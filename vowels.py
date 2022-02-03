def removeVowels(str):

    vowels = ("a", "e", "i", "o", "u")

    x = ""
    for i in str:
        if i not in vowels:
            x += i

    return x



print(removeVowels("whatever"))





