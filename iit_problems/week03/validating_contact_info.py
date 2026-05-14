import re
name = input("Your name: ")
phone = input("Your phone number: ")
email = input("Your email: ")
address = input("Your address: ")
match_phone = re.search(r"\d{9,12}+", phone)
email_pattern = r"^[\w.]+@\w+\.\w+"
match_email = re.search(email_pattern, email)
print(f"\n\nHi {name},\nYou have entered the following details\nPhone number: {match_phone[0]}\nEmail address: {match_email[0]}\nAddress: {address}\nPlease be kind to confirm the above details")