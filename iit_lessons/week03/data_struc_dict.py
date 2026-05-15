student_details = {
    "name": "John",
    "age": "22",
    "department": "PDU"
}
# print(student_details)

# Changing the value assigned to key "name"
# student_details['name'] = "Patrick"
# print(student_details)

# Assigning a dictionary as a value to key "name"

student_details['name'] = {
    "first_name" : "John",
    "surname" : "Williams"
}
# print(student_details['name']['surname'])


sample_dict = {
    "name": {
        "first_name": '',
        "second_name": '',
        "surname": {
            "father's_maiden_name": '',
            "mother's_maiden_name": {
                "real_mother_maiden_name": '',
                "step_mother's_maiden_name": ''
            }
        }
    },
    "age": "22",
    "department": "PDU"
}
import json
print(json.dumps(sample_dict, indent = 4))

