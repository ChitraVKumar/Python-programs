def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_math(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_math(cube, [1, 2, 3, 4])

print(squares)


def html_tags(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_f1 = html_tags('H1')  # print_f1 is a function behaves as a calling function for html tags
print_f1('Headline! ')

print_f2 = html_tags('p')  # print_f2 is a function behaves as a calling function for html tags
print_f2('Paragraph text.')
