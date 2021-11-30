# -*- coding: utf-8 -*-
from random import randint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DepressionError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class SuicideError(Exception):
    pass


def record_an_error(error):
    with open('Phil_Connors_days.log', mode='a') as file:
        file.write(f'{error}\n')


def one_dey():
    exception_list = {1: IamGodError, 2: DepressionError, 3: DrunkError, 4: CarCrashError, 5: GluttonyError,
                      6: SuicideError}
    karma_quantity = randint(1, 7)
    cube = randint(1, 13)
    if cube == 13:
        cube = randint(1, 6)
        raise exception_list[cube]
    return karma_quantity


ENLIGHTENMENT_CARMA_LEVEL = 777
carma_level = 0
day = 0
while True:
    try:
        day += 1
        carma_level += one_dey()
        if carma_level >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except IamGodError as exc:
        print('Фил возомнил себя богом')
        record_an_error(exc.__class__.__name__)
    except DrunkError as exc:
        print('Фил упился в усмерть')
        record_an_error(exc.__class__.__name__)
    except DepressionError as exc:
        print('Фил  тосковал весь день')
        record_an_error(exc.__class__.__name__)
    except CarCrashError as exc:
        print('Фил  катался на машине')
        record_an_error(exc.__class__.__name__)
    except GluttonyError as exc:
        print('Фил  не следил за калориями')
        record_an_error(exc.__class__.__name__)
    except SuicideError as exc:
        print('Фил  наложил на себя руки')
        record_an_error(exc.__class__.__name__)
print(f'Филу понадобилось {day} дней, для того, чтобы познать дзен и разрушить порочный круг!!!')
# https://goo.gl/JnsDqu333
