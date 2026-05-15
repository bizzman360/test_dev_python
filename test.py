from datetime import datetime
seconds = 0

for i in range(5):
    this_sec = int(datetime.now().strftime("%S"))
    while True:
        next_sec = int(datetime.now().strftime("%S"))
        if next_sec == this_sec+2:
            seconds = seconds + 2
            print(f"{seconds} seconds passed by")
            break