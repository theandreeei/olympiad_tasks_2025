'''
Робота: Мордач Андрій, 10-А, школа номер 23
Повна версія (як модуль, де всі завдання) знаходиться на https://github.com/theandreeei/olympiad_tasks_2025
'''
from validations import validation_for_a, validation_for_b, validation_for_c, validation_for_d


def natural_numbers_count(n: int):
    # Validation
    validation_for_a(n)
    # Code
    return n - 1


def splitted_texts_by_numbers(n: int, text:str, ignore_empty_text=False):
    # Validation
    validation_for_b(n, text, ignore_empty_text)
    # Code
    return ''.join(f'{text}+' for _ in range(n))[:-1]


def minutes_to_time(m: int):
    # Validation
    validation_for_c(m)
    # Code
    hours = int(m / 60)
    minutes = m - hours * 60
    return f'{hours} {minutes}'


def number_powers_count(a: int, b: int):
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
