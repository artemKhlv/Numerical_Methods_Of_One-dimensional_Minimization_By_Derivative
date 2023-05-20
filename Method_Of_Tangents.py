import math

call_count = 0
call_count_def = 0
call_count_def2 = 0


def f(x):
    global call_count
    call_count += 1
    return 1 * pow(x, 2) + 1 / math.atan(x)


def derivative(x):
    global call_count_def
    call_count_def += 1
    return 2 * x - 1 / ((x ** 2 + 1) * pow(math.atan(x), 2))


def derivative2(x):
    global call_count_def2
    call_count_def2 += 1
    return (2 * x * math.atan(x) + 2) / ((pow(x, 4) + 2 * pow(x, 2) + 1) * pow(math.atan(x), 3))


def tangent_method():
    iter_count = 0
    a = A
    b = B
    epsi = EPSI
    k = 0
    x_k = (a + b) / 2
    while True:
        iter_count += 1
        f_d1 = derivative(x_k)
        if abs(f_d1) <= epsi:
            return x_k, iter_count
        if abs(f_d1) > epsi:
            f_d2 = derivative2(x_k)
            if f_d2 > 0:
                x_k1 = x_k - (f_d1 / f_d2)
                while not a <= x_k1 <= b:
                    x_k1 = (x_k + x_k1) / 2
                x_k = x_k1
                k += 1
            else:
                raise ValueError("Обязательное условие f''(x_k) > 0 нарушено.")


A = 0.2
B = 2
EPSI = 0.0005
min, iters = tangent_method()
print("Число итераций: ", iters)
print("Количество вычислений функции: ", call_count)
print("Количество вычислений первой производной: ", call_count_def)
print("Количество вычислений второй производной: ", call_count_def2)
print("Найденное решение (min): ", min)
print("Значение функции: ", f(min))


