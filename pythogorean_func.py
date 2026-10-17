# Запросить у пользователя размеры катетов
# Вычисляем гипотенузу и выводим на экран

import math

def hypotenuse(a, b):
    hyp = math.sqrt(a ** 2 + b ** 2)
    return hyp

x1 = float(input("Введите длину первого катета: "))
x2 = float(input("Введите длину второго катета: "))
hyp = hypotenuse(x1, x2)
print(hyp)
print("Вот длина гипотенузы!")

