import re
text = "My number is 0771234567"
match = re.search(r"\d+", text)
print(match[0])