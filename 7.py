k = int(input('Введите количество суши: '))
for i in range(0,(k//5)+1):
    for j in range(0, (k//7)+1):
        if k == i*5 + j*7:
            print('да')
            break
    else:
        continue
    break
else:
    print('нет')