from random import randint


def show_field(field):
    for i in field:
        print(*i)
def create_field(cnt, h, w):
    field = [[0 for i in range(width)] for j in range(height)]
    while cnt:
        y = randint(0, width - 1)
        x = randint(0, height - 1)
        if field[x][y] == 0:
            field[x][y] = 'X'
            cnt -= 1
    for i in range(h):
        for j in range(w):
            if field[i][j] != 'X':
                for ai in (i - 1, i, i + 1):
                    for aj in (j - 1, j, j + 1):
                        try:
                            if ai != -1 and aj != -1 and field[ai][aj] == 'X':
                                field[i][j] += 1
                        except IndexError:
                            pass
    return field
print('Введите размеры поля')
height = int(input('Высота: '))
width = int(input('Ширина: '))
count_bomb = int(input('Укажите колличество бомб: '))
field_user = [['*' for i in range(width)] for j in range(height)]
show_field(field_user)
field = create_field(count_bomb, height, width)
print('Поле сформировано')

while True:
    x, y = map(int, input('Укажите координаты через пробел(x y): ').split())
    if field[y][x] == 'X':
        show_field(field_user)
        print('Вы проиграли!\nИгра окончена.')
        break
    elif field[y][x] == 0:
        for ay in (y - 1, y, y + 1):
            for ax in (x - 1, x, x + 1):
                if ay != -1 and ax != -1:
                    try:
                        field_user[ay][ax] = field[ay][ax]
                    except IndexError: pass
        show_field(field_user)
    else:
        field_user[y][x] = field[y][x]
        show_field(field_user)
    cnt = 0
    for i in field_user:
        cnt += i.count('*')
    if cnt == count_bomb:
        print('\n')
        show_field(field)
        print('\nПоздравляю, Вы победили!!!')
        break