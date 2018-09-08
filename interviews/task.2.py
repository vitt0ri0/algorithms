# на входе 2 массива.
# вывести на выходе пересечение этих двух массивов (элементы, которые встречаются в каждом массиве).

# Пример:
# m1 [1, 2, 3, 2, 0]
# m2 [5, 1, 2, 7, 3, 2]
#
# result [1, 2, 2, 3]


def union_of_arrays(arr1, arr2):
    # let's sort both arrays
    arr1.sort()
    arr2.sort()

    # iterators for arr1, arr2
    a = 0
    b = 0
    # result
    union = []

    # then go along both arrays
    while a < len(arr1) and b < len(arr2):
        # if an element is lower than another, increment iterator in that array
        if arr1[a] < arr2[b]:
            a += 1
        elif arr1[a] > arr2[b]:
            b += 1
        else:
            # if we find equal elements
            union.append(arr1[a])  # add element to the result
            # increment iterators of both arrays
            a += 1
            b += 1

    return union


if __name__ == "__main__":
    # test cases
    arr1 = [1, 2, 3, 2, 0]
    arr2 = [5, 1, 2, 7, 3, 2]
    print(union_of_arrays(arr1, arr2))