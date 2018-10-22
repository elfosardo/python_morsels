def add(*lists_of_int):
    add_list = []

    for blah in zip(*lists_of_int):
        element = [sum(k) for k in zip(*blah)]
        add_list.append(element)

    return add_list


if __name__ == '__main__':
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]

    print(add(matrix1, matrix2))

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

    print(add(matrix1, matrix2))

    print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))
