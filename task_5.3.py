N = int(input('Введите число от 1 до 9: ')) 

for i in range(N+1):
    if i == 0:
        continue
    print(i, end='')