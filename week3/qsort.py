def quick_sort(array):
    """
    Implement quick sort.
    """

    if len(array) <= 1:
        return array, 0
    pivot_idx = choose_pivot(array)
    l, p, r = partition(array, pivot_idx)
    l, m1 = quick_sort(l)
    r, m2 = quick_sort(r)
    return (l + [p] + r), (len(l) + len(r) + m1 + m2)


def choose_pivot(array):
    """
    Return first/last/median pivot.

    Output:
        pivot index(int)
    """
    # pivot_index = 0
    # pivot_index = len(array) - 1
    # return pivot_index

    first = 0
    last = -1
    if len(array) % 2 == 0:
        mid = int(len(array) / 2) - 1
    else:
        mid = int(len(array) / 2)

    vals = [array[first], array[mid], array[last]]
    vals.sort()
    index = [first, mid, last]
    for i in index:
        if array[i] == vals[1]:
            return i


def partition(array, pivot_idx):
    """
    Partition array accroding to pivot.
    """
    if pivot_idx != 0:
        array[0], array[pivot_idx] = array[pivot_idx], array[0]

    p = array[0]
    i = 1
    for j in range(i, len(array)):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return array[: i - 1], array[i - 1], array[i:]


if __name__ == "__main__":
    input_array = []
    with open("week3\QuickSort.txt", "r") as fh:
        for i in fh:
            input_array.append(int(i))
    sorted_array, count = quick_sort(input_array)
    print("Total comparsion:", count)
    print("Correct sort:", sorted_array == [i + 1 for i in range(len(input_array))])
