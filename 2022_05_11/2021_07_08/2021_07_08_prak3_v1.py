import time
import threading


FILE_NAME = '2021_07_08_input.txt'


def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def save_numbers(numbers, fn_rule, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        for number in numbers:
            if fn_rule(number):
                f.write(str(number))
                f.write('\n')


L = []
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    text_numbers = f.readlines()
    L = list(map(int, text_numbers))
print(L)

th1 = threading.Thread(
    target=save_numbers,
    args=(L, is_even, '2021_07_08_output_even.txt')
)
th2 = threading.Thread(
    target=save_numbers,
    args=(L, is_odd, '2021_07_08_output_odd.txt')
)

start = time.perf_counter()
th1.start()
th2.start()
th1.join()
th2.join()
finish = time.perf_counter()
print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
