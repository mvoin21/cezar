
nmbrs = input('Введите числа через пробел: ')
moving = int(input('Введите значение для сдвига: '))

def get_cezar(m, nmbrs):
    nmbrs_list = nmbrs.split(' ')
    result = []
    for item in nmbrs_list:
        if m >= 0:
            result.append(nmbrs_list[nmbrs_list.index(item) - m])
        else:
            result.append(nmbrs_list[nmbrs_list.index(item) + (m-1)])

    return f'Result: {result}'

print(cezar(moving, nmbrs))
