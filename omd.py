# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Оказалось, что у утки лапки и зонт она держать не умеет, от этого ей еще больше захотелось в бар.')


def step2_no_umbrella():
    print('Дождь не пошел и забытый зонтик не помешал утке насладиться барной атмосферной.')


if __name__ == '__main__':
    step1()
