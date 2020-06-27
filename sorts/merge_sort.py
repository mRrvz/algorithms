from random import randint
from numpy import array
from utils import check_correctness


def merge(left, right):
    res = []
    i = j = 0

    for k in range(len(left) + len(right)):
        if i == len(right):
            return res + left[j:]

        if j == len(left):
            return res + right[i:]

        if right[i] <= left[j]:
            res.append(right[i])
            i = i + 1
        else:
            res.append(left[j])
            j = j + 1

    return res


def merge_sort(arr):
    if len(arr) >= 2:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge(left, right)
    else:
        return arr


def main():
    arr = [randint(1, 100) for i in range(10)]
    arr = merge_sort(arr)

    if check_correctness(arr):
        print("MERGE SORT OK")
    else:
        print("MERGE SORT FAIL")
                
                
if __name__ == "__main__":
    main()

