import re
text = "My contact number is 94-770-123456"
match = re.sub(r"-","", text)
print(match)