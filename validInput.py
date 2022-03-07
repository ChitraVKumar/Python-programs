while True:
    print("Enter your Age: ")
    age = input()
    if age.isdecimal():
        break
    print("Enter a valid Age!")

while True:
    print("Please enter a password with only letters and numbers")
    password = input()
    if password.isalnum():
        break
    print("Enter a valid password with letters and numbers only!")