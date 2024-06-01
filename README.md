# EcoTrack
## Overview
EcoTrack is a backend system tailored for monitoring a diverse array of sensors. It facilitates the oversight of environmental data gathered by these sensors and also plays a pivotal role in managing the workers responsible for monitoring these sensors
## Features

- **User Management**: This feature lets admins handle user accounts. They can create, change, or delete user profiles.

- **Sensor Management**: With this, users can manage sensors easily. They can add, update, or remove sensors, and also get data from them.

- **Alert Monitoring**: Keeps an eye on sensor data and alerts users if something's wrong. They can see, edit, or fix these alerts in the system.

- **Data Monitoring**: Helps users get sensor data easily.

- **Permission Control**: Controls who can access what. Admins have full access, while others only see what they're supposed to.

- **Real-time Monitoring**: Shows sensor data and alerts in real-time. This helps users stay updated on environmental conditions.

- **Location Tracking**: Lets users see where sensors and equipment are. They can see where everything is and find important areas.

- **Security**: Keeps data safe and makes sure only the right people can access it. It uses special tools to protect information from being seen or changed by unauthorized people.

- **Customization**: Allows users to change and add things to fit their needs. They can make the system work just right for them.

## Endpoints

### Sensors Endpoints

- **GET** `/sensors/alerts/{id}/`: Retrieve details of a specific alert.
- **PUT** `/sensors/alerts/{id}/`: Update details of a specific alert.
- **PATCH** `/sensors/alerts/{id}/`: Partially update details of a specific alert.
- **DELETE** `/sensors/alerts/{id}/`: Delete a specific alert.
- **DELETE** `/sensors/alerts/{id}/delete/`: Alias for deleting a specific alert.
- **PUT** `/sensors/alerts/{id}/update/`: Alias for updating a specific alert.
- **PATCH** `/sensors/alerts/{id}/update/`: Alias for partially updating a specific alert.
- **POST** `/sensors/create/`: Create a new sensor.
- **GET** `/sensors/data/`: Retrieve a list of all sensor data.
- **POST** `/sensors/data/create/`: Create a new sensor data entry.
- **GET** `/sensors/data/{id}/`: Retrieve details of a specific sensor data entry.
- **PUT** `/sensors/data/{id}/`: Update details of a specific sensor data entry.
- **PATCH** `/sensors/data/{id}/`: Partially update details of a specific sensor data entry.
- **DELETE** `/sensors/data/{id}/`: Delete a specific sensor data entry.
- **PATCH** `/sensors/data/{id}/update/`: Alias for partially updating a specific sensor data entry.
- **GET** `/sensors/list/`: Retrieve a list of all sensors.
- **GET** `/sensors/list_high_danger/`: Retrieve a list of sensors with high danger alerts.
- **GET** `/sensors/list_low_danger/`: Retrieve a list of sensors with low danger alerts.
- **GET** `/sensors/list_medium_danger/`: Retrieve a list of sensors with medium danger alerts.
- **GET** `/sensors/list_no_danger/`: Retrieve a list of sensors with no danger alerts.
- **GET** `/sensors/list_of_active_sensors/`: Retrieve a list of active sensors.
- **GET** `/sensors/list_of_alerts/`: Retrieve a list of alerts associated with sensors.
- **GET** `/sensors/list_of_inactive_sensors/`: Retrieve a list of inactive sensors.
- **GET** `/sensors/list_of_maintenance_sensors/`: Retrieve a list of sensors under maintenance.
- **GET** `/sensors/{id}/`: Retrieve details of a specific sensor.
- **PUT** `/sensors/{id}/`: Update details of a specific sensor.
- **PATCH** `/sensors/{id}/`: Partially update details of a specific sensor.
- **DELETE** `/sensors/{id}/`: Delete a specific sensor.
- **DELETE** `/sensors/{id}/delete/`: Alias for deleting a specific sensor.
- **PUT** `/sensors/{id}/update/`: Alias for updating a specific sensor.
- **PATCH** `/sensors/{id}/update/`: Alias for partially updating a specific sensor.

### Users Endpoints

- **GET** `/users/`: Retrieve a list of all users.
- **POST** `/users/create/`: Create a new user.
- **GET** `/users/{id}/`: Retrieve details of a specific user.
- **DELETE** `/users/{id}/delete`: Alias for deleting a specific user.
- **PUT** `/users/{id}/update/`: Alias for updating a specific user.
- **PATCH** `/users/{id}/update/`: Alias for partially updating a specific user.
  
## Data Models

### User

Represents user profiles in the system.

#### Fields

- **username**: The username for the user.
- **email**: The email address of the user.
- **password**: The password of the user.
- **first_name**: The first name of the user.
- **last_name**: The last name of the user.
- **phone_number**: The phone number of the user.
- **birth_date**: The birth date of the user.
- **address**: The address of the user.
- **position**: The position of the user.
- **hire_date**: The hire date of the user.
- **bio**: A short biography or description of the user.
- **is_active**: Indicates whether the user is active or not.
- **role**: The role of the user (Admin or Worker).
- **groups**: The groups the user belongs to.
- **user_permissions**: The permissions assigned to the user.

### Sensor

Represents sensors used for monitoring environmental data.

### Fields

- **name**: The name of the sensor.
- **type**: The type of sensor.
- **model**: The model of the sensor.
- **location**: The location where the sensor is installed.
- **installation_date**: The date when the sensor was installed.
- **status**: The status of the sensor (Active, Inactive, Maintenance).
- **responsible**: The user responsible for the sensor.
- **description**: Description of the sensor.
- **timestamp**: The timestamp when the sensor data was recorded.

### Sensor_Data

Represents data collected by sensors.

#### Fields

- **sensor**: Reference to the sensor.
- **pm25**: Particulate Matter (PM2.5) measurement.
- **pm10**: Particulate Matter (PM10) measurement.
- **co2**: Carbon Dioxide (CO2) measurement.
- **temperature**: Temperature measurement.
- **humidity**: Humidity measurement.
- **pressure**: Atmospheric pressure measurement.
- **wind_speed**: Wind speed measurement.
- **timestamp**: The timestamp when the data was recorded.

### Alert

Represents alerts generated by sensors.

#### Fields

- **sensor**: Reference to the sensor associated with the alert.
- **description**: Description of the alert.
- **last_timestamp**: The timestamp when the alert was last updated.
- **last_timecheckedby**: The user who last checked the alert.
- **warning_notes**: Additional notes or comments regarding the alert.
- **severity**: The severity level of the alert (High, Medium, Low, Ok).


## User Groups and Permissions

#### Admin
- **Permissions**:
  - Managment(CREAT, READ, DELETE, UPDATE) of sensors.
  - Managment(CREAT, READ, DELETE, UPDATE) of alerts.
  - Managment(CREAT, READ, DELETE, UPDATE) of data.
  - Managment(CREAT, READ, DELETE, UPDATE) worker users.
  - etc...

#### Worker
- **Permissions**:
  - Can change alerts.
  - Can view alerts.
  - Can view data.
  - Can view profile.


## Screenshots and Video Demonstration

[Video Demonstration](https://drive.google.com/drive/u/0/folders/1z899_lDDABPkst9nNfLR5fuXBMbcUeY2)


Sensors related endpoints 

![ ](https://github.com/kaydurgu/ecotrack/blob/main/sreens/Screenshot_21.png)

Users related endpoints 

![ ](https://github.com/kaydurgu/ecotrack/blob/main/sreens/Screenshot_22.png)

- **GET** `/users/`: Retrieve a list of all users.

![ ](https://github.com/kaydurgu/ecotrack/blob/main/sreens/Screenshot_23.png)

- **GET** `/sensors/list/`: Retrieve a list of all sensors.
  
![ ](https://github.com/kaydurgu/ecotrack/blob/main/sreens/Screenshot_24.png)

- **GET** `/sensors/alerts/{id}/`: Retrieve details of a specific alert.

![ ](https://github.com/kaydurgu/ecotrack/blob/main/sreens/25.png)


## Getting Started

To run the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/kaydurgu/ecotrack.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables for API keys and database configurations.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributors

- Bakytbek uulu Zhanbolot

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
