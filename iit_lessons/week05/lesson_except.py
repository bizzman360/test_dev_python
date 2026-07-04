# try and common exception
# try:
#     number = int(input("Enter a number: "))
#     division = int(input("Enter the division: "))
#     result = number / division
#     print(result)
# except Exception as e:
#     print(e)

def calculate():
    try:
        number = int(input("Enter a number: "))
        division = int(input("Enter the division: "))
        if division <= 0:
            raise Exception("Enter a value greater than 0")
        result = number / division
        return result
    except Exception as e:
        print(e)
        calculate()
        
    
result = calculate()
print(result)

#try and raising exception
def calculate():
    try:
        number = int(input("Enter a number: "))
        division = int(input("Enter the division: "))
        if division <= 0:
            raise Exception("Enter a value greater than 0")
        result = number / division
        return result
    except Exception as e:
        print(e)
        calculate()
        
    
result = calculate()
print(result)
    