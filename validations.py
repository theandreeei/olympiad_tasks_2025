import sys


# Individual Validations
def validation_for_a(n: int):
    is_int(n)
    if n <= 0:
        _exit('Аргумент n має бути більшим за 1.')
    if n > 10**18: 
        _exit('Аргумент n має бути не більшим за 10^18.')


def validation_for_b(n: int, text: str, ignore_empty_text: bool):
    is_int(n)
    if n <= 0:
        _exit('Аргумент n має бути більшим за 0.')
    if not isinstance(text, str):
        _exit('Аргумент text має бути тільки типом str (текстом).')
    if not text.strip() and not ignore_empty_text:  # NOTE: або замість умови not text.strip() написати text == "", щоб можна було отримати результат "  +  +  +  ".
        _exit('Аргумент text з типом str не повинен бути порожнім.')


def validation_for_c(m: int):
    is_int(m)
    if not 0 <= m < 1440:
        _exit('Аргумент m має бути в діапазоні від 0 (включно) до 1440.')


def validation_for_d(a: int, b: int):
    is_int(a)
    is_int(b)
    if not 1 <= a <= b:
        _exit('Аргументи a, b мають бути в одному рядку через промiжок (1 ≤ a ≤ b).')


def validation_for_e(numbers_str: str):
    if not isinstance(numbers_str, str):
        _exit('Аргумент numbers_str повинен бути тільки типом str, наприклад "1 3 5 7 9 11".')
    try:
        numbers = [int(i) for i in numbers_str.split()]
    except ValueError as e:
        _exit(f'Зауважте, що елементи в аргументу numbers_str повинні бути тільки цілими: "1 3 5 7 9 11". Приклад неправильних варіантів: "1 3.3 5 7 \'9\' 11". Подробиці: {e}')
    return numbers


def validation_for_f(m: int):
    is_int(m)
    if not 0 <= m <= 20:
        _exit(f'Аргумент m має бути в діапазоні від 0 включно до 20 включно.')


# Casual Validations
def is_int(n):
    success = isinstance(n, int)
    if not success: _exit('Аргумент має бути тільки типом int (числом).')


# Exit
def _exit(message):
    # print(f'Помилка:\n{message}')  # NOTE: Альтернатива, тоді sys.exit(1).
    sys.exit(message)
