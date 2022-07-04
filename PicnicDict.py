picnicDict = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}


def printPicnic(picItems, left, right):
    print("PICNIC ITEMS".center(left + right, '*'))
    for k, v in picItems.items():
        print(k.ljust(left, '-') + str(v).rjust(right))

printPicnic(picnicDict, 20, 6)

