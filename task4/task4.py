N = int(input())
S = input()

def mediana(str:str):
    if str.count("0") > str.count("1"):
        return 0
    elif str.count("0") < str.count("1"):
        return 1
    else:
        return 0.5

def print_mediana(S):
    print(-1)
    for index in range(2, len(S) + 1):
        res = -1
        for l in range(1, index):
                slice = S[l - 1 : index]
                if mediana(slice) == int(S[index - 1]):
                    res = l
                    break
        print(res)

print_mediana(S)


