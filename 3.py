n, m = map(float, input().split('x'))
k = int(input())

if (((n*m)-n) == k) or (((n*m)-m) == k):
    print('Успешно')
else:
    print('Не осуществимо')