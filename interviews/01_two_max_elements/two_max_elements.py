# Write a function which finds two max elements from an array.
#
# example:
# array [1.1, 2.2, 3.3, 4.4, 5.5]
# output [5.5, 4.4]


def two_max_elements(array):

    if len(array) < 2:
        raise Exception()

    # take first two elements
    max1 = array[0]
    max2 = array[1]

    # put them in descending order, if they are not
    if max2 > max1:
        temp = max2
        max2 = max1
        max1 = temp

    # for every element starting from 3rd
    for x in range(2, len(array)):

        el = array[x]
        if el > max1:
            max2 = max1
            max1 = el
        elif el > max2:
            max2 = el

    return max1, max2


if __name__ == "__main__":
    # some test cases
    array = [1.1, 2.2, 3.3]
    print(two_max_elements(array))

    array = [1.1, 2.2, 3.3, 5.5, 4.4]
    print(two_max_elements(array))