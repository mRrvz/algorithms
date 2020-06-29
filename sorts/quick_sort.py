from random import randint
from utils import check_correctness


def partition(arr, p, r):
    pivot = arr[r - 1]
    i = p - 1

    for j in range(p, r):
        if arr[j] < pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i + 1], arr[r - 1] = arr[r - 1], arr[i + 1]
    return i + 1


def quick_sort(arr):
    def __quick_sort(arr, p, r):
        if p < r:
            q = partition(arr, p, r)
            __quick_sort(arr, p, q - 1)
            __quick_sort(arr, q + 1, r)

    __quick_sort(arr, 0, len(arr))



def main():
    arr = [randint(-10, 10) for i in range(10)]
    print(arr)
    quick_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
