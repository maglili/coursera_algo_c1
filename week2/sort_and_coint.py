def sort_and_count(array, length):
    """
    Given a list, find its inversion.
    """
    if length == 1:
        return array, 0
    else:
        # sort
        n = round(length / 2)
        B, X = sort_and_count(array[:n], n)
        C, Y = sort_and_count(array[n:], length - n)

        # merge
        i = j = 0
        count = 0
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
                count += len(B[i:])

        return sorted_list, count + X + Y


if __name__ == "__main__":
    import time

    with open("IntegerArray.txt", encoding="utf-8") as fh:
        input_array = []
        for row in fh:
            input_array.append(int(row))

    # input_array = [8,7,6,5,4,3,2,1]
    start = time.time()
    _, ans = sort_and_count(input_array, len(input_array))
    print("ans:", ans)
    print("time:", time.time() - start)
