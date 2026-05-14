#Write a python code to prompt the user with the exact following questions
#Name of the first person in the vehicle:
#Name of the second person in the vehicle:
#Name of the third person in the vehicle:
#The unit of speed:

#Print the exact following statement with the relevant attributes replaced accordingly
#[person01_name],", [person02_name] and", [person03_name] is travelling at speed", [speed(Km/h)] in their vehicle

person01 = input('Name of the first person in the vehicle: ')
person02 = input('Name of the second person in the vehicle: ')
person03 = input('Name of the third person in the vehicle: ')
speed = input("The speed at which the vehicle is travelling: ")
unit = input("The unit of speed: ")
print(f"{person01},", f"{person02} and", f"{person03} is travelling at speed", f"{speed}({unit}) in their vehicle")