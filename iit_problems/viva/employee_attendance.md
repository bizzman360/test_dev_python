# Create a python server that listens and expects query parameters

In your assignments folder, create an app called "time_in_time_out.py". Create a python server that listens and expects the time in and timeout details of employees as query parameters. The following details must be expected.

1. employee id (integer)
2. time in or time out in 24 hrs clock

You must refer to the given employee database in .csv format and validate the entered entries. If the employee id doesn't exist, the application should return "employee unavailable" or else the application should record the data in a file called "attendance.csv" with the following details

| timestamp | employee_id | employee_name | time_in | time_out |
| --------- | ----------- | ------------- | ------- | -------- |
|           |             |               |         |          |
|           |             |               |         |          |

You can get the current timestamp using the following code

```Python
from datetime import datetime

now = datetime.now() 
```
