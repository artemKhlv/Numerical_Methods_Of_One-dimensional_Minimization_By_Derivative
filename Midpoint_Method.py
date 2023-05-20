import math

call_count = 0
call_count_def = 0


def function(x):
    global call_count
    call_count += 1
    return x ** 2 + 1/(math.atan(x))


def derivative(x):
    global call_count_def
    call_count_def += 1
    return 2*x - 1/((x**2 + 1) * pow(math.atan(x), 2))


def middle_point_method():
    iter_count = 0
    a = A
    b = B
    epsi = EPSI
    k = 0
    while True:
        iter_count += 1
        x_n = (a + b) / 2
        f_prime = derivative(x_n)
        if abs(f_prime) <= epsi:
            return x_n, iter_count
        elif f_prime > 0:
            b = x_n
        else:
            a = x_n
        k += 1


A = 0.2
B = 2
EPSI = 0.0005
min, iters = middle_point_method()
print("Число итераций: ", iters)
print("Количество вычислений функции: ", call_count)
print("Количество вычислений производной функции: ", call_count_def)
print("Найденное решение (min): ", min)
print("Значение функции: ", function(min))

