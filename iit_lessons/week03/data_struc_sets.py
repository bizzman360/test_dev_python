student_ids = {"sid99535", "sid11298", "sid79728"}
student_ids.add("sid02774")
print(student_ids)
student_ids.remove("sid99535")
print(student_ids)

# Adding the same value will replace the existing value
# student_ids.add("sid11298")
# print(student_ids)

student_ids.update(['sid64980', 'sid33985'])
print(student_ids)