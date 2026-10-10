weights = [0.1, 1.1, 0.3, 0.8, 0.5, 2.2, 3.1, 1.7, 0.4]

# найти самое большое и самое малое значения в списке и вывести их на экран

max = weights[0]
min = weights[0]

for n in weights:
    if n > max:
        max = n

    if n < min:
        min = n

print(f"Максимальное значение: {max}")
print(f"Минимальное значение: {min}")