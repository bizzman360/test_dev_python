from datetime import datetime
seconds = 0

delay = int(input("What is the delay? "))
min_ = 0

for i in range(30):
    this_sec = int(datetime.now().strftime("%S"))
    print(this_sec)
    while True:
        next_sec = int(datetime.now().strftime("%S"))
        if next_sec == 0:
            next_sec = 60
        if next_sec == this_sec+delay:
            seconds = seconds + delay
            print(f"{seconds} seconds passed by")
            break