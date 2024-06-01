from rest_framework import serializers


from .models import UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id', 'last_login', 'is_superuser', 'username', 'email', 'is_staff',
            'date_joined', 'first_name', 'last_name', 'is_active', 'groups', 'user_permissions'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'password', 'first_name', 'last_name',
            'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login',
            'groups', 'user_permissions'
        ]
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined', 'last_login', 'user_permissions']

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user