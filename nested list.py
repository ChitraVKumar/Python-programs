# import copy
#
# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# students.sort(key= lambda x:x[0])
# students1 = copy.copy(students)
# students1.sort(key=lambda x:x[1])
# student2 = copy.copy(students1)
# print(student2)

# students.sort(key=lambda x:x[1])

# print(students)

# y = sorted(students, key=lambda x:(x[0], x[1]))
# y.reverse()

# print(y)
all_scores = []
marksheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    all_scores.append(score)
    marksheet.append([name, score])

# print(all_scores)
# print(marksheet)

sorted_score = list(set(all_scores))  # second-lowest score
second_lowest = sorted(sorted_score)[1]
# print(second_lowest)

res = []
for name, score in marksheet:
    if score == second_lowest:
        res.append(name)
res.sort()
for i in res:
    print(i)