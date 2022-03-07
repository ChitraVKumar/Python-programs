def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    elif number%2 == 1:
        x = 3 * number + 1
        print(x)
        return x
    


try:
    n = int(input("Enter an Integer: "))
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('Enter Integers ONLY.')