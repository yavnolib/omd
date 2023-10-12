"""
    This script provides the ability
    to analyze an input csv file
    containing information about company employees

    File format:
    - Full name;department;team;job title;mark;salary
"""

import os
from typing import Callable, Dict, Union

INPUT_FNAME = 'Corp_Summary.csv'
OUTPUT_FNAME = 'output.csv'


def read_file(fname: str) -> list:
    """
        Function for reading file
    """
    with open(fname, mode='r', encoding='UTF-8') as csv_table:
        res = [i.strip().split(';') for i in csv_table]
    return res[1:]


def interactive_menu(src_file: list) -> None:
    """
        Main function of the program.

        Calls up an interactive menu
        with which you can call up the corresponding functions
    """

    running = True
    title = '\nВыберите режим работы программы:\n'
    info = '1 - вывести иерархию команд\n' \
        + '2 - вывести сводный отчёт по депараментам\n' \
        + '3 - сохранить сводный отчет из пункта 2 в csv\n'

    interactive = 'Введите номер: '

    while running:
        option = ''
        while option not in MODES:
            option = input(title + info + interactive)

        MODES[option](src_file)

        continue_options = {'да': True, 'нет': False,
                            'lf': True, 'ytn': False}
        continue_option = ''
        while continue_option not in continue_options:
            continue_option = input('Продолжить?\nДа/нет: ').lower()
        running = continue_options[continue_option]


def first_mode(src_file: list) -> None:
    """
        Function to display command hierarchy
    """
    dep_team: Dict[str, list] = {}
    for line in src_file:
        department = line[1]
        team = line[2]
        if department in dep_team:
            prev_teams = dep_team[department]
            if team not in prev_teams:
                prev_teams.append(team)
        else:
            dep_team.update({department: [team]})

    print('\n\tИерархия команд:\n')
    for num, (key, value) in enumerate(dep_team.items()):
        print(f'{num + 1}) {key}:\n\t{", ".join(value)}')


def second_mode(src_file: list, save: bool = False,
                save_fname: Union[str, bytes, os.PathLike] = '') -> None:
    """
        A function that provides the ability
        to display a summary report
        by department with the ability to save it to a csv file

        You MUST be sure to PASS the name of the output file
        if save=True
        otherwise you should NOT DO IT
    """
    assert not (save ^ (save_fname != '')),\
        'Не передано имя файла' if save\
        else 'Лишняя передача имени файла, т.к. сохранение отключено'

    dep_info: Dict[str, tuple] = {}
    for line in src_file:
        department = line[1]
        salary = int(line[-1])
        if department in dep_info:
            headcount, min_s, max_s, mean_s = dep_info[department]
            mean_s = (mean_s * headcount + salary) / (headcount + 1)
            headcount += 1
            max_s = salary if salary > max_s else max_s
            min_s = salary if salary < min_s else min_s
            dep_info.update({department: (headcount, min_s,
                                          max_s, mean_s)})
        else:
            headcount = 1
            min_s = max_s = mean_s = salary
            dep_info.update({department: (headcount, min_s,
                                          max_s, mean_s)})
    if not save:
        print('\n\tСводный отчет по департаментам:\n')
        print('Департамент, Численность, Вилка зарплат, Средняя зарплата')
        for key, val in dep_info.items():
            print(f'{key}, {val[0]}, {val[1]}—{val[2]}₽, {val[3]:.2f}₽')
    else:
        result = [
            ['Департамент', 'Численность',
             'Мин.зарплата', 'Макс.зарплата', 'Сред.зарплата']
        ]

        for key, val in dep_info.items():
            result.append([key, *list(map(str, val))])

        with open(save_fname, mode='w', encoding='UTF-8') as output:
            output.write('\n'.join([';'.join(i) for i in result]))


def third_mode(src_file: list) -> None:
    """
        A function that calls the
        second_mode function
        with the necessary parameters to save the result to a file
    """
    second_mode(src_file, save=True, save_fname=OUTPUT_FNAME)
    print('Сохранено!')


MODES: Dict[str, Callable] = {'1': first_mode,
                              '2': second_mode,
                              '3': third_mode}

if __name__ == '__main__':
    file = read_file(INPUT_FNAME)
    interactive_menu(file)
