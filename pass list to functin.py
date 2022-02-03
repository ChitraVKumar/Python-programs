
list = [20, 25, 14, 19, 16, 24, 28, 47, 26]

def count(list):
    even = 0
    odd = 0

    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

even, odd = count(list)

print("Even: {} and Odd: {}". format(even, odd))

