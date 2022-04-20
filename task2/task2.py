height, width = map(int, input().split())

my_map = ""
for _ in range(height):
    my_map += input()

columns_with_letters = set()
for i in range(height):
    for j in range(width):
        if my_map[i * width + j].isalpha():
            columns_with_letters.add(j)

for i in range(height - 1, -1, -1):
    for j in range(width - 1, -1, -1):
        if j not in columns_with_letters:
            if i < height - 1:
                print(my_map[(i + 1) * width + j], end='') # опускаем столбцы без букв, так как стоят не на своих местах
            else:
                print(".", end='')
        else:
            print(my_map[i * width + j], end='')
    print()