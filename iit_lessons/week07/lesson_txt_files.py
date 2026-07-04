# ========================================= #

# import json
# file = open("about_pdu.txt", 'r')
# content = file.read()
# print(content)
# file.close()

# ========================================= #

# data = {}
# i = 0
# for line in file:          
#     data[f"line_{i}"]=line.strip()
#     i += 1

# print(json.dumps(data, indent=2))
# file.close

# ========================================= #

# import os

# folder = "my_folder"
# file_path = os.path.join(folder, "sample_file.txt")

# os.makedirs(folder, exist_ok=True)

# file = open(file_path, "w")
# file.write("Hello world")
# file.close()

# ========================================= #

# folder = "my_folder"
# file_path = os.path.join(folder, "sample_file.txt")

# os.makedirs(folder, exist_ok=True)

# with open(file_path, "w") as f:
#     f.write("Dear PDU students,\n\nYou have now written a simple text into a document\n\nBest,\nLucky")

# ========================================= #

# folder = "my_folder"
# file_path = os.path.join(folder, "sample_file.py")

# os.makedirs(folder, exist_ok=True)

# with open(file_path, "w") as f:
#     f.write("print(\"This is a sample. Here I'm going to declare variables and perform mathematical calculations\")\n\ntotal = 2+2\nprint('The total is '+str(total))")

# ========================================= #

# file1 = open("about_pdu.txt")
# file2 = open("about_you.txt")

# data1 = file1.read()
# data2 = file2.read()

# print(data1)
# print("\n\n\n")
# print(data2)

# file1.close()
# file2.close()

# ========================================= #

# with open("about_pdu.txt") as file1, \
#     open("about_you.txt") as file2:

#     data1 = file1.read()
#     data2 = file2.read()

#     print(data1)
#     print("\n\n\n")
#     print(data2)

# ========================================= #

# file = open("about_pdu.txt", "a")
# file.write("\n\nPDU at IIT is a great place to learn and acquire new skills useful for my professional carrier")
# file.close()

# ========================================= #

# with open("about_pdu.txt", "a") as file:
#     file.write("\n\nPDU at IIT is a great place to learn and acquire new skills useful for my professional carrier")