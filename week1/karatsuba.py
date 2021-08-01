def karatsuba(x: int, y: int) -> int:
    """
    Implement karatsuba multiplication.
    """
    # base case
    if (x < 10) or (y < 10):
        return x * y

    # recursive
    else:
        n = len(str(max(x, y)))
        n_2 = round(n / 2)

        # calc coeffient
        a = x // (10 ** n_2)
        b = x % (10 ** n_2)
        c = y // (10 ** n_2)
        d = y % (10 ** n_2)

        # recursion
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd

        return ac * 10 ** (2 * n_2) + ad_bc * 10 ** (n_2) + bd


if __name__ == "__main__":
    import time

    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627

    start_time = time.time()
    my_ans = karatsuba(a, b)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    py_ans = a * b
    print("--- %s seconds ---" % (time.time() - start_time))

    print(my_ans)
    print(py_ans)
    print("Correct:", my_ans == py_ans)
