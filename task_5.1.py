s = int(input('Введите число: '))  

if (s%3 or s%5) == 0:
    print('Fizz Buzz')
elif s%3 == 0:
    print('Fizz')
elif s%5 == 0:
    print('Buzz')
else:
    print(s)

