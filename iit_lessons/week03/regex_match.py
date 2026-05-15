import re
text = "Hello world"
match = re.match(r"Hello", text)
# print(match[0])
#ERROR WITH THE FOLLOWING CODE BECAUSE re.match ONLY COMPARE THE FIRST VALUE IN THE STRING
# match = re.match(r"world", text)
print(match[0])