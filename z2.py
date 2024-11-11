#3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

import random

NUMBER_OF_CELLS = 8
FIRST_CELL = 1
LUCKY_MATCHES = 4
BOARD = [1, 2, 3, 4, 5, 6, 7, 8]



def input_coordinate_cells():
    cells = []

    for _ in range(NUMBER_OF_CELLS):
        coordinate = [int(cell) for cell in input().split()]
        cells.append(coordinate)

    return cells


def check_coordinate_cells(cells):
    is_correct = True
    for i in range(NUMBER_OF_CELLS):
        x1, y1 = cells[i]
        for j in range(i + 1, NUMBER_OF_CELLS):
            x2, y2 = cells[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                is_correct = False

    return True if is_correct else False


def random_fill_cells():
    cells = []

    for _ in range(NUMBER_OF_CELLS):
        coordinate = random.choice(BOARD), random.choice(BOARD)
        cells.append(coordinate)

    return cells


def check_lucky_matches():
    count_match = 0
    matches = []

    while count_match < LUCKY_MATCHES:
        cells = random_fill_cells()

        if check_coordinate_cells(cells):
            count_match += 1
            matches.append(cells)

    return matches


def show_matches(matches):
    for line in matches:
        print(line)


if __name__ == '__main__':
    # cells = input_coordinate_cells()
    cells = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
    print(check_coordinate_cells(cells))

    matches = check_lucky_matches()
    show_matches(matches)