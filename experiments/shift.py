# Shifts all list elements to the left by one position.
# The first element will become the last,
# the 3rd element will become the 2nd,
# the 4th element will become the 3rd, and so on.
#
#      →→→→→→→→→→→→→→→→→→→→→→→
#     ↑                       ↓
#   +---+---+---+---+---+---+---+
#   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
#   +---+---+---+---+---+---+---+
#       ←   ←   ←   ←   ←   ←
#
#                🠗🠗🠗
#
#   +---+---+---+---+---+---+---+
#   | 2 | 3 | 4 | 5 | 6 | 7 | 1 |
#   +---+---+---+---+---+---+---+
#
# Example: [] -> []
# Example: [1] -> [1]
# Example: [1,2] -> [2,1]
# Example: [1,2,3] -> [2,3,1]
# Example: [1,2,3,4,5,6,7,8,9] -> [2,3,4,5,6,7,8,9,1]


def shift_reverse(list):
    output = []
    if len(list) == 0:
        return output
    for i in range(len(list)):
        output.append(list[i - 1])
    return output


def shift_while(list):
    output = []
    if len(list) == 0:
        return output
    i = 1
    while i < len(list):
        output.append(list[i])
        i = i + 1
    output.append(list[0])
    return output


def shift_for(list):
    output = []
    if len(list) == 0:
        return output
    for i in range(1, len(list)):
        output.append(list[i])
    output.append(list[0])
    return output


def shift_slices(list):
    output = []
    if len(list) > 0:
        output.extend(list[1:])
        output.append(list[0])
    return output


def shift_inplace_smart(list):
    list.append(list.pop(0))


def shift_inplace_stupid(list):
    # Тут надо явно проверить размер списка чтобы избежать ошибок,
    # потому что дальше мы читаем/пишем элемент по индексу 0 и -1.
    if len(list) < 2:
        return list
    a = list[0]  # Запоминаем первый элемент до того,
    # как он будет стерт сдвигом остальных элементов
    # на его место в следующем цикле.
    for i in range(0, len(list) - 1):
        list[i] = list[i + 1]
    list[-1] = a  # Записываем то, что было первым на последее место.
