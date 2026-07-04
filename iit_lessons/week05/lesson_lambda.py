# upper = lambda text: text.upper()
# result = upper("good morning")

# print(result)

import re

names = ["John", "Erica", "Julia", "Jonathan", "Peter"]
rate_per_hour = "USD 0.2"

result = lambda name, age: float(re.search(r"\d+\.\d+", rate_per_hour).group())* age if name in names else "Not available"
print(round(result("John", 41)),2)
