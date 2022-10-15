def _min(n):
    mn = int(n[0])
    for i in range(len(n)):
        if int(n[i]) < mn:
            mn = int(n[i])
    return mn


def _max(n):
    mx = 0
    for i in range(len(n)):
        if int(n[i]) > mx:
            mx = int(n[i])
    return mx


def _mult(n):
    pr = 1
    for i in range(len(n)):
        pr = pr * int(n[i])
    return pr


def _sum(n):
    sm = 0
    for i in range(len(n)):
        sm = sm + int(n[i])
    return sm


def _fca(n):
    try:
        n = int(n)
    except ValueError:
        return 'Такой функции нет, перезапустите программу'
    else:
        if n > 4 or n < 1:
            return 'Такой функции нет, перезапустите программу'
        else:
            return n


def st():
    file = input('Введите название файла:')
    f = open(file, "r")
    a = f.read().split()
    print('Выберите функцию:\n1 - Поиск максимального числа\n2 - Поиск минимального числа'
          '\n3 - Произведение всех чисел в файле\n4 - Сумма всех чисел в файле')
    start = input()
    if _fca(start) == 'Такой функции нет, перезапустите программу':
        print(_fca(start))

    if _fca(start) == 1:
        print(_max(a))
    if _fca(start) == 2:
        print(_min(a))
    if _fca(start) == 3:
        print(_mult(a))
    if _fca(start) == 4:
        print(_sum(a))


if __name__ == '__main__':
    st()
