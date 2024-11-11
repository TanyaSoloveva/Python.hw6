#3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random as rd
import timeit

__all__ = ['main']


def __chess(matrix: list[list[int]]) -> bool:
    MAX_NUMBER = 8
    rezul = []

    for (x, y) in [map(list, zip(*matrix))]:
        if len(set(y)) == len(set(x)) == MAX_NUMBER:
            for i in range(MAX_NUMBER):
                for j in range(i + 1, MAX_NUMBER):
                    rezul.extend([abs(y[i] - y[j]) == abs(x[i] - x[j])])
    return False if any(rezul) or len(rezul) < 1 else True


def __gener_num() -> map:
    x = [x for x in range(1, 9)]
    y = [x for x in range(1, 9)]
    rd.shuffle(x)
    rd.shuffle(y)
    return map(list, zip(x, y))


def main() -> str:
    def _step() -> None:
        coun = 4
        COUNT = 0
        lis = []
        while coun:
            _gener = [*__gener_num()]
            if __chess(_gener):
                lis.append(_gener)
                coun -= 1
            COUNT += 1
        print(f'Всего генераций {COUNT}:')
        for x in lis:
            print(x)

    return f'{timeit.timeit(lambda: _step(), number=1):.2f} сек. было затрачено'


if __name__ == '__main__':
    print(main())