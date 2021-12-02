# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class Registration:

    def __init__(self, file, file_registrations_bad, file_registrations_good):
        self.file = file
        self.file_registrations_bad = file_registrations_bad
        self.file_registrations_good = file_registrations_good

    def registration_error(self, line):
        if len(line.split()) == 3:
            name, email, age = line.split(' ')
            if not name.isalpha():
                raise NotNameError('поле имени содержит Не только буквы!')
            if not 9 < int(age) < 99 or not age.isdigit():
                raise ValueError('поле возраст НЕ является числом от 10 до 99!')
            if ('@ ' and '.') not in email:
                raise NotEmailError('поле емейл НЕ содержит @ и .(точку)!')
        else:
            raise ValueError('НЕ присутсвуют все три поля!')

    def registration(self):
        with open(self.file, 'r') as ff:
            for line in ff:
                line = line[:-1]
                try:
                    self.registration_error(line)
                    with open(self.file_registrations_good, mode='a', encoding='utf-8') as file:
                        file.write(line + '\n')
                    continue
                except ValueError as exc:
                    print(line, exc)
                except NotNameError as exc:
                    print(line, exc)
                except NotEmailError as exc:
                    print(line, exc)
                with open(self.file_registrations_bad, mode='a', encoding='utf-8') as file:
                    file.write(line + '\n')


check = Registration(file='registrations.txt', file_registrations_bad='registrations_bad.log',
                     file_registrations_good='registrations_good.log')
check.registration()
