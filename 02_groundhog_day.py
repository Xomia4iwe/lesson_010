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


def one_dey():
    exception_list = {1: IamGodError, 2: DepressionError, 3: DrunkError, 4: CarCrashError, 5: GluttonyError,
                      6: SuicideError}
    karma_quantity = randint(1, 7)
    cube = randint(1, 13)
    if cube == 13:
        cube = randint(1, 6)
        raise exception_list[cube]
    return karma_quantity


# https://goo.gl/JnsDqu333
