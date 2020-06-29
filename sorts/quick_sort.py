from random import randint
from utils import check_correctness


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr):
    def __quick_sort(arr, p, r):
        if p < r:
            q = partition(arr, p, r)
            __quick_sort(arr, p, q - 1)
            __quick_sort(arr, q + 1, r)

    __quick_sort(arr, 0, len(arr) - 1)



def main():
    print(arr := [randint(-10, 10) for i in range(10)])
    quick_sort(arr)
    
    if check_correctness(arr):
        print("QSORT IS OK")
    else:
        print("QSORT FAIL")


if __name__ == "__main__":
    main()
