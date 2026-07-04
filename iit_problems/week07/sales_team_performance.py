import csv
entries = []
performance_low = []
performance_medium = []
performance_high = []
performance_elite = []

try:
    def get_data():
        while True:
            name = input("Sales person's name: ")
            while True:
                sale = int(input("Monthly sale value: "))
                if sale >= 10000:
                    break
                else:
                    print('Amount is too low. You are fired :(')
                    break
            if sale >=10000:
                entries.append({"Name":name, "Monthly sale value":sale})

    def enter_data():
        with open("./iit_problems/week07/monthly_sales.csv", "w", newline='') as f:
            headers = ['Name', 'Monthly sale value']

            writer = csv.DictWriter(f, fieldnames=headers)

            writer.writeheader()
            writer.writerows(entries)

    def categorize():
        for item in entries:
            if 10000 <= item['Monthly sale value'] < 100000:
                performance_low.append(item['Name'])
            elif 100000 <= item['Monthly sale value'] < 500000:
                performance_medium.append(item['Name'])
            elif 500000 <= item['Monthly sale value'] < 1000000:
                performance_high.append(item['Name'])
            elif 1000000 <= item['Monthly sale value']:
                performance_elite.append(item['Name'])

        max_count = max(len(performance_low), len(performance_medium), len(performance_high), len(performance_elite))

        with open("./iit_problems/week07/categorised.csv", "w", newline="") as c:
            headers = ['Low', 'Medium', 'High', 'Elite']
            writer = csv.DictWriter(c, fieldnames=headers)
            writer.writeheader()

            categorized_entries = []
            for i in range(max_count):
                categorized_entries.append({
                    "Low": performance_low[i] if i < len(performance_low) else "",
                    "Medium": performance_medium[i] if i < len(performance_medium) else "",
                    "High": performance_high[i] if i < len(performance_high) else "",
                    "Elite": performance_elite[i] if i < len(performance_elite) else "",
                    })
            writer.writerows(categorized_entries)

    get_data()                
except EOFError:
    if len(entries) > 0:
            enter_data()
            categorize()
    else:
        print('There are no entries to enter')
        get_data()

except Exception as e:
    print(e)