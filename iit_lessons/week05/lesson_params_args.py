#Positional arguments
# def greetings(name, surname):
#     print(f"Hello {name} {surname}")

# greetings("John", "Lathem")

#Keyword arguments
# greetings(surname="Lathem", name="John")

#Default parameters
# def greetings(name="David", surname="Beckham"):
#     print(f"Hello {name} {surname}")

# greetings(surname="Lathem", name="John")
# greetings()

#Variable-length arguments

# def names(*names):
#     for i in names:
#         print(i)

# names("John", "Liam", "Erica", "Fedrick")

# def calculate(*numbers):
#     print(sum(numbers))

# calculate(10,20,30,40,50,60)

def student_details(**details):
    print(details)
    # for i in details.items():
    #     print(i)
    # for i in details.items():
    #     print(i[0])

student_details(name="George", age="20", course="Python")