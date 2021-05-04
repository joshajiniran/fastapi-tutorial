import phone_checker

print("Welcome to our call center\n")
callee = input("Enter phone number to call: ")

if phone_checker.check_phone_number_correct(callee) is True:
    print("Calling {}...".format(callee))
else:
    print("Please check if phone number is correct")
