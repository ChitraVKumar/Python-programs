def fibonacci(n):
    a = 0
    b = 1

    if n<=0:
        print("Invalid input. Enter a valid input: ")

    elif n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if(c<=n): # to print values within the given n value
                print(c)
            else:
                pass


fibonacci(100)








