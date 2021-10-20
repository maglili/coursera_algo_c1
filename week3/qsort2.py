def partition(arr, l, r):
    pivot = arr[l]  # pivot
    i = l + 1
    for j in range(i, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1


def quickSort(arr, l, r):
    if len(arr) == 1:
        return arr
    if l < r:
        pi = partition(arr, l, r)
        print(pi)
        quickSort(arr, l, pi)
        quickSort(arr, pi + 1, r)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
