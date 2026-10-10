values = [29.0, 25.0, 26.5, 23.0, 24.8, 29.9, 21.0, 28.2, 22.3, 21.1, 25.1, 21.4, 23.0, 27.2]

# Сделать чтобы максимальное значение было на последнем месте,
# при этом все значения остались в списке (неважно на каких позициях).

# print(values)

# temp = values[13] # 29.0
# values[13] = values[6]
# values[6] = temp
#
# print(values)

max = values[0]
idx_max = 0

for i in range(len(values)):
    # n === values[i]
    # print(values[i])
    if values[i] > max: # если да, то нужно обновить адреса/пароли/явки максимального элемента
        max = values[i]
        idx_max = i

idx_last = len(values) - 1
temp = values[idx_last]
values[idx_last] = values[idx_max]
values[idx_max] = temp

print(values)