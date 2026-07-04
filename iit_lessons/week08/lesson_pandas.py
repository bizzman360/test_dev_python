import pandas as pd

df = pd.read_csv('./iit_lessons/week08/student database.csv')
# print(df)
# print(type(df))

# print(df.head(1))
# print(df.tail(3))
# print(df['Stream'])
# print(df[['Stream', 'z score']])
# print(df[df['z score'] > 2])
# print(df['z score'].mean())
# print(df['z score'].max())
# print(df.sort_values('z score'))
# print(df.sort_values('z score', ascending=False))

# df = df.sort_values('z score')
# df.to_csv('./iit_lessons/week08/student database.csv', index=False)


#==================================#

# import pandas as pd

# df = pd.read_excel('./iit_lessons/week08/student_database.xlsx')
# df = pd.read_excel('./iit_lessons/week08/student_database.xlsx', sheet_name='Clubs_Activities')
# df = pd.read_excel('./iit_lessons/week08/student_database.xlsx', sheet_name='Clubs_Activities', usecols='A:C')
# df = df['ActivityName']

# print(df)

df = df.sort_values('YearsActive')
with pd.ExcelWriter('./iit_lessons/week08/student_database.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name='Sorted activities', index=False)