place = input()

right_l = ['a', 'c', 'e', 'g']
wrong_l = ['b', 'd', 'f', 'h']
num = int(place[-1])
letter = place[0]

if letter in right_l:
    if num % 2 != 0:
        print('Чёрный')
    else:
        print('Белый')
elif letter in wrong_l:
    if num % 2 != 0:
        print('Белый')
    else:
        print('Чёрный')