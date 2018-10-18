
def compact(sequence):
    """Return an iterator with adjacent duplicate values removed"""

    element_before = object()
    for element in sequence:
        if element != element_before:
            yield element
            element_before = element


if __name__ == '__main__':
    print(compact([1, 1, 1]))
    print(compact([1, 1, 2, 2, 3, 2]))
    print(compact([]))
    print(compact([1, 1, 1, 1, 1, 1]))
    print(compact([1, 1, 2, 2, 3]))
    nums = iter([1, 2, 3])
    print(next(nums))
    print(x for x in (compact(nums)))
    print(next(nums))
