birthdays = {'Alice': 'Apr 1','Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input("Enter a name: (Blak space to quit)")
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of" + name)
    
    else:
        print('I do not have birthday information for ' + name) 
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday 
        print('Birthday database updated.')


