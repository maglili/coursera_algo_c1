def merge_sort(array, length):
    """
    Implement merge sort algo.
    Time complexity: O(n*log(n))
    """

    # base case
    if length == 1:
        return array
    # recursive
    else:
        # sort
        n = round(length / 2)
        B = merge_sort(array[:n], n)
        C = merge_sort(array[n:], length - n)

        # merge
        i = j = 0
        sorted_list = []
        for _ in range(length):
            # avoid out of index
            if i == len(B):
                sorted_list += C[j:]
                break
            elif j == len(C):
                sorted_list += B[i:]
                break

            if B[i] < C[j]:
                sorted_list.append(B[i])
                i += 1
            else:
                sorted_list.append(C[j])
                j += 1

        return sorted_list


if __name__ == "__main__":
    import time

    input_array = [8, 7, 6, 5, 4, 3, 2, 1]
    start = time.time()
    ans = merge_sort(input_array, len(input_array))
    print("input:", input_array)
    print("ans  :", ans)
    print("time :", time.time() - start)
