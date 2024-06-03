# weather-forecasting-platform FrontEnd

This folder contains all the code related to the frontend of the weather application, developed using the Django framework. Here you will find all the files necessary for the user interface, including templates, static files (CSS, JavaScript, images), and frontend configurations.

## Folder contents
- `forecasting_weather/`: This folder contains the views and static files related to the weather forecast
- `templates/`: This folder contains the HTML files that define the structure and layout of the application's web pages.
- `static/`: Static files such as CSS, JavaScript and images that are used by HTML pages are stored here.
- `views.py`: File where the views that control the presentation logic of the application are defined.
- `urls.py`: Website navigation paths configuration file.

## Website Navigation Map

### Public Pages

1. **Home Page**
 - URL: `home/`
 - Description: Welcome page that provides general information about the weather app and invites users to register or log in.

2. **User Registration**
 - URL: `/register/`
 - Description: Registration form where new users can create an account.

### Private Pages (require authentication)

3. **Current Weather**
 - URL: `/current-weather/`
 - Description: Displays the current weather information for the location selected by the user.

4. **Weather Forecast**
 - URL: `/forecast/`
 - Description: Provides a forecast of the future weather for the location selected by the user.

### Administrator Pages (require authentication and administrator permissions)

5. **User Management**
 - URL: `/admin/users/`
 - Description: Allows the administrator to view and manage the users registered in the application.