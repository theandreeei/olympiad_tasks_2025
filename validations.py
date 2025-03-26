import sys


# Individual Validations
def validation_for_a(n):
    is_int(n)
    if n <= 1:
        _exit('Аргумент n має бути більшим за 1.')


def validation_for_b(n, text, ignore_empty_text):
    is_int(n)
    if n <= 1:
        _exit('Аргумент n має бути більшим за 1.')
    if not isinstance(text, str):
        _exit('Аргумент text має бути тільки типом str (текстом).')
    if not text.strip() and not ignore_empty_text:  # NOTE: або замість умови not text.strip() написати text == "", щоб можна було отримати результат "  +  +  +  ".
        _exit('Аргумент text з типом str не повинен бути порожнім.')


def validation_for_c(m):
    is_int(m)
    if not 0 < m < 1440:
        _exit('Аргумент m має бути в діапазоні від 0 до 1440.')


def validation_for_d(a, b):
    is_int(a)
    is_int(b)
    if not 1 <= a <= b:
        _exit('Аргументи a, b мають бути в одному рядку через промiжок (1 ≤ a ≤ b)')


# Casual Validations
def is_int(n):
    success = isinstance(n, int)
    if not success: _exit('Аргумент має бути тільки типом int (числом).')


# Exit
def _exit(message):
    print(f'Помилка:\n{message}')
    sys.exit(1)
