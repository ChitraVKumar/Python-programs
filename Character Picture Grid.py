grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# for j in range(5, -1, -1):
#     for x in range(len(grid)):
#         print(grid[x][j], end = " ")
#     print()


# list = [[1,2,3],[4,5,6],[7,8,9]]

# for x in range(len(list)):
#     for j in range(len(list[x])):
#         print(list[j][x], end=" ")
#     print()


# for x in range(len(list)):
#     print(list[x], end=" ")
#     print()

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end =" ")
    print()

# list = list[::-1]
# for x in range(len(list)):
#     print(list[x], end = " ")
#     print()

