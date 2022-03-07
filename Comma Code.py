# Comma Code


def comma_code(list):
    for i in range(len(list)-2):
        print(list[i], end=", ")
    print(list[-2] + " " + "and" + " " + list[-1])
      

spam =["apples", "bananas", "tofu", "cats"]
comma_code(spam)


