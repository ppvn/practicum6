a, b = map(int, input('Введите размер отверстия: ').split('x'))
c, d, e = map(int, input('Введите размер кирпича: ').split('x'))

brick_v = [c, d, e]
brick_v.remove(max(brick_v))

d_hole = (a**2 + b**2)**0.5
d_brick = ((brick_v[0])**2 + (brick_v[1])**2)**0.5

if d_hole > d_brick:
    print('Да')
else:
    print('Нет')