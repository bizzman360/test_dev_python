winner_name = input("Winners name: ")
winner_timing = input("Winner's timing: ")
winner_country = input("Winner's country: ")
runnerup_name = input("Runner-up name: ")
runnerup_timing = input("Runner-up timing: ")
runnerup_country = input("Runner-up country: ")
thirdPlace_name = input("Third place name: ")
thirdPlace_timing = input("Third place timing: ")
thirdPlace_country = input("Third place country: ")
winner_dict = {
    "name": winner_name,
    "timing": winner_timing,
    "country": winner_country
}
runnerup_dict = {
    "name": runnerup_name,
    "timing": runnerup_timing,
    "country": runnerup_country
}
thirdPlace_dict = {
    "name": thirdPlace_name,
    "timing": thirdPlace_timing,
    "country": thirdPlace_country
}
results = []
results.append(winner_dict)
results.append(runnerup_dict)
results.append(thirdPlace_dict)

import json
print(json.dumps(results, indent=3))