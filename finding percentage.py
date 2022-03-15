from functools import reduce
# import statistics
n = int(input("Enter the number of students: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter name and marks: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
print(scores)
query_name = input("Enter a name to find the average of: ")


def average(list):
    avg = reduce(lambda x, y: x + y, list) / len(list)
    return avg

marks = student_marks[query_name]
print("{:.2f}".format(average(marks)))


# Harsh 25 26.5 28
# Anurag 26 28 30