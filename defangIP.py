

def defangIPaddr(address):

    newstr = ""  # new string

    for i in range(len(address)):

        # adding dot with square brackets in new string
        if address[i] == '.':
            newstr += '[.]'

        # adding character other than dots in new string
        else:
            newstr += address[i]
    return newstr

print("255.0.1.1")


