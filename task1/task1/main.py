import math
n = int(input())
nums = map(int, input().split())


a = ord('a')
result = ""
letters = []
prev = 0
cur = 0

for letter in range(a, a + 26):
    letters.append(chr(letter))
letters.append(' ')

for num in nums:
    cur = num
    xor = cur^prev
    index_letter = math.log2(xor)
    result += letters[int(index_letter)]
    prev = cur

print(result)





