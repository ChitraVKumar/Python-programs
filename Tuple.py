from functools import reduce

list = [25.0, 26.5, 28]
avg = reduce(lambda x, y: x + y, list) / len(list)

print("{:.2f}".format(avg))
