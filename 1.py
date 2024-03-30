r = 6.5

a, b = map(float, input().split('x'))
hd = ((a ** 2 + b ** 2) ** 0.5) / 2

if hd > r:
    print('Нет')
elif hd < r:
    print('Да')
