arr = [0.1, 1.1, 0.3, 0.8, 0.5, 2.2, 3.1, 0.7, 0.4]
arr2 = [0.3, 1.1, 0.3, 0.8, 0.5, 7.2, 3.1, 0.7, 9.14]


# Index of maximal element is $__
def find_index_of_max(list):
    idx_max = 0
    max = list[idx_max]

    for n in list:
        if n > max:
            max = n

    for i in range(len(list)):
        if list[i] == max:
            idx_max = i

    return idx_max

id1 = find_index_of_max(arr)
id2 = find_index_of_max(arr2)

print(id1, id2)


