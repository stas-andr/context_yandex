width = 14
height = 8

map = """\
.............
...._........
.._/A\_..._..
./B\_/D\_/F\.
.\_/C\_/E\_/.
...\_/G\_/...
.....\_/.....
.............
"""
print(len(map))
columns_with_letters = set()
for i in range(height):
    for j in range(width):
        if map[i * width + j].isalpha():
            columns_with_letters.add(j)
        print(map[i * width + j], end='')

print('between')
for i in range(height - 1, -1, -1):
    for j in range(width - 1, -1, -1):
        if j in columns_with_letters:
            if i > 0:
                print(map[(i - 1) * width + j], end='') # поднимаем столбцец с буквами
            else:
                print(".", end='')
        else:
            print(map[i * width + j], end='')

print("columns_with_letters = ", columns_with_letters)