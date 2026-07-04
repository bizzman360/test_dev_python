from datetime import datetime

no_of_students = int(input("How many students have enrolled for the python class?"))

for i in range(no_of_students):
    now = datetime.now().strftime("%H:%M:%S")
    