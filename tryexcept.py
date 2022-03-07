# def spam(divide):
#     try:
#         return 42/divide
#     except ZeroDivisionError:
#         print(
#             'Error: Invalid argument!'
#         )

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(42))
# print(spam(3))

def divideBy(Num):
    return 42/Num
try:
    print(divideBy(2))
    print(divideBy(12))
    print(divideBy(0))
    print(divideBy(42))
    print(divideBy(3))
except ZeroDivisionError:
    print("Error: Invalid!")