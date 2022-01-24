def romanToInt( s: str):
    # s = "MCMXCIV"
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    x = 0

    for i in range(len(s)):
        if i + 1 < len(s) and table[s[i]] < table[s[i+1]]:
            x -= table[s[i]]
        else:
            x += table[s[i]]

    return x

print(romanToInt("MCMXCIV"))



