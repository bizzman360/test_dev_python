# from openpyxl import load_workbook

# workbook = load_workbook("./iit_lessons/week08/student_database.xlsx")
# sheet = workbook["Students"]
# print(sheet['A1'].value)

#=======================================#

# from openpyxl import load_workbook

# workbook = load_workbook("./iit_lessons/week08/student_database.xlsx")
# sheet = workbook["Students"]

# for row in sheet.iter_rows(values_only=True):
#     print(row)
#     break

#=======================================#

# from openpyxl import Workbook

# wb = Workbook()

# sheet = wb.active
# sheet.title = 'Sample_data'
# sheet['A1'] = 'Name'
# sheet['B1'] = 'Salary'

# sheet.append(['John', 150000])
# wb.save('./iit_lessons/week08/salaries.xlsx')

#=======================================#

# from openpyxl import Workbook

# wb = Workbook()
# sheet = wb.active
# sheet.title = 'sample_data'

# data = [{
#     "Name": "John",
#     "Salary": 150000
# },
# {
#     "Name": "Eric",
#     "Salary": 250000
# }]

# sheet.append(list(data[0].keys()))

# for item in data:
#     sheet.append(list(item.values()))

# wb.save('./iit_lessons/week08/salaries.xlsx')

#=======================================#

# from openpyxl import Workbook

# wb = Workbook()
# sheet = wb.active
# sheet.title = 'sample_data'

# data = [{
#     "Name": "John",
#     "Salary": 150000
# },
# {
#     "Name": "Eric",
#     "Salary": 250000
# }]

# sheet.append(list(data[0].keys()))

# for item in data:
#     sheet.append([
#         item["Name"],
#         item["Salary"]
#     ])

# wb.save('./iit_lessons/week08/salaries.xlsx')

#=======================================#

# from openpyxl import Workbook

# wb = Workbook()
# sheet = wb.active
# sheet.title = 'sample_data'

# data = [{
#     "Name": "John",
#     "Salary": 150000
# },
# {
#     "Name": "Eric",
#     "Salary": 250000
# }]

# headers = data[0].keys()
# sheet.append(list(headers))

# for item in data:
#     sheet.append([item[h] for h in headers])

# wb.save('./iit_lessons/week08/salaries.xlsx')