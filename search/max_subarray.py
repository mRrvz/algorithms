from random import randint
from math import inf


def max_crossing(arr, l, m, h):
    lind = m
    lsum = -inf
    sum_ = 0

    for i in range(m, l - 1, -1):
        sum_ += arr[i]
        if sum_ > lsum:
            lsum = sum_
            lind = i

    rind = m
    rsum = -inf
    sum_ = 0

    for i in range(m + 1, h):
        sum_ += arr[i]
        if sum_ > rsum:
            rsum = sum_
            rind = i

    return lind, rind, rsum + lsum


def max_subarray(arr, l, h):
    if l != h:
        mid = (l + h) // 2

        ll, lh, lsum = max_subarray(arr, l, mid)
        rl, rh, rsum = max_subarray(arr, mid + 1, h)
        cl, ch, csum = max_crossing(arr, l, mid, h + 1)
        
        if lsum >= rsum and lsum >= csum:
            return ll, lh, lsum
        elif rsum >= lsum and rsum >= csum:
            return rl, rh, rsum
        else:
            return cl, ch, csum
    else:
        return l, h, arr[l]


def main():
    arr = [randint(-10, 10) for x in range(10)]
    print("ARRAY: ", arr, "\nRESULT:", max_subarray(arr, 0, len(arr) - 1))


if __name__ == "__main__":
    main()
