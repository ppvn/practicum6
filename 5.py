movement = input()
l1, num1 = movement[0], int(movement[1])
l2, num2 = movement[-2], int(movement[-1])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
right = (3**2 + 2**2)**0.5

a = letters.index(l1)
b = letters.index(l2)

if ((abs(a-b)+1)**2 + (abs(num1 - num2) + 1)**2)**0.5 == right:
    print('Верно')
else:
    print('Ошибка')