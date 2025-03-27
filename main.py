'''
Робота: Мордач Андрій, 10-А, школа номер 23
Повна версія (як модуль, де всі завдання) знаходиться на https://github.com/theandreeei/olympiad_tasks_2025
'''
from typing import Union
from validations import validation_for_a, validation_for_b, validation_for_c, validation_for_d, validation_for_e, validation_for_f


def natural_numbers_count(n: int) -> int:
    '''
    Програма на входi приймає натуральне число n. Потрiбно вивести кiлькiсть нату-
    ральних чисел менших n.

    Аргументи: n: int - натуральне число.
    Повертає: число, int.
    '''
    # Validation
    validation_for_a(n)

    # Code
    return n - 1


def splitted_texts_by_numbers(n: int, text: str, ignore_empty_text: bool = False) -> str:
    '''
    На вхiд програми подається натуральне число n та деякий текст, наприклад Real.
    Потрiбно повторити цей текст n раз в одному рядку, роздiливши копiї символом плюс "+".

    Аргументи: n: int - натуральне число;
               text: str - текст з латинських лiтер;
               ignore_empty_text: bool = False - можливість допускати пусті тексти (аргумент text). За замовчуванням False.
    Повертає: текст, str.
    '''
    # Validation
    validation_for_b(n, text, ignore_empty_text)

    # Code
    return ''.join(f'{text}+' for _ in range(n))[:-1]


def minutes_to_time(m: int) -> str:
    '''
    Вiд початку доби пройшло m хвилин. Скільки годин i хвилин показує годинник на цей момент?

    Аргументи: m: int - ціле число, хв.
    Повертає: два числа, str.
    '''
    # Validation
    validation_for_c(m)

    # Code
    hours = int(m / 60)
    minutes = m - hours * 60
    return f'{hours} {minutes}'


def number_powers_count(a: int, b: int) -> int:
    '''
    Потрiбно знайти i вивести кiлькiсть степенiв двiйки, що лежать на вiдрiзку [a,b]. Одиниця, як 2⁰ = 1 не враховується. (1 ≤ a ≤ b).

    Аргументи: a: int - натуральне число;
               b: int - натуральне число.
    Повертає: число, int.
    '''
    # Validation
    validation_for_d(a, b)

    # Code
    current_power = 1
    result = 0

    while 2 ** current_power <= b:
        if not 2 ** current_power < a: 
            result += 1

        current_power += 1
    return result 


def find_max_and_paired_number(numbers_str: str) -> Union[int, str]:
    '''
    Дано масив з n цiлих чисел. Знайти найбiльше парне число. Якщо таких чисел не iснує виведiть NO.

    Аргументи: numbers_str: str - список виду тексту (наприклад: "1 3 5 7 9 11").
    Повертає: число, int або "NO", str.

    NOTE: Ми передаємо тільки список виду тексту, наприклад "1 3 5 7 9 11" - як дано в умові. Зокрема в умові потрібно вказувати кількість чисел у списку (n), але через можливості Python для успішного виконання коду (що було перевірено), це нам не потрібно.
    '''
    # Validation and Get
    numbers = validation_for_e(numbers_str)

    # Code
    filtered_numbers = [i for i in numbers if i % 2 == 0]
    return max(filtered_numbers) if len(filtered_numbers) > 0 else 'NO'


def all_double_sum_numbers(m: int) -> str:
    '''
    Вивести всi двозначнi числа, що складаються з рiзних цифр, сума яких дорiвнює m.

    Аргументи: m: int - натуральне число (0 ≤ m ≤ 20).
    Повертає: список чисел у виді тексту або "No", str.
    '''
    # Validation
    validation_for_f(m)

    # Code
    results = []
    for i in range(10, 100):
        if int(str(i)[0]) + int(str(i)[1]) == m and str(i)[0] != str(i)[1]:
            results.append(i)
    return ' '.join(map(str, results)) if len(results) > 0 else 'No'


if __name__ == '__main__':
    # A
    print('Завдання А:')
    result = natural_numbers_count(123)
    print(result)
    
    # B
    print('\nЗавдання B:')
    result = splitted_texts_by_numbers(4, 'Real')
    print(result)

    # C
    print('\nЗавдання C:')
    result = minutes_to_time(127)
    print(result)

    # D
    print('\nЗавдання D:')
    result = number_powers_count(4, 34)
    print(result)

    # E
    print('\nЗавдання E:')
    result = find_max_and_paired_number('2 3 5 6 1')
    print(result)

    # F
    print('\nЗавдання F:')
    result = all_double_sum_numbers(4)
    print(result)
