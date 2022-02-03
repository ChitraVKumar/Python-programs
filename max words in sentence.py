sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

result = 0

for i in sentences:
    y = len(i.split(" "))
    if y > result:
        result = y

print(result)




