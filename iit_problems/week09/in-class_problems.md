# Get the weather update

In your assignments folder, create an app called "weather_now.py". Use HTTP GET method to get current weather details of your location. You may search for latitude and logitude data of your current location on the internet and pass them to the following url to get the details. The details must be indented and clearly shown in the TERMINAL

WEATHER URL: [api.open-meteo.com/v1/forecast?latitude=6.9271&amp;longitude=79.8612¤t_weather=true](https://api.open-meteo.com/v1/forecast?latitude=6.9271&longitude=79.8612&current_weather=true)

# Student database

In your assignments folder, create an app called "student_database.py".  Create a python server that listens and expects the following student data through query parameters. 

* student_id (integer. 6 digits)
* student_name (string)
* course_enrolled (string)

Write the data received into a pandas dataframe and write the student data into a file called student_database.xlsx, after sorting the data in ascending order of student ids. You must validate the received and respond with an appropriate error message if the wrong data is entered.
