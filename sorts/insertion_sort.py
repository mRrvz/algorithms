from random import random
from numpy import array
from utils import check_correctness


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    arr = array([random() for i in range(10)])
    insertion_sort(arr)

    if check_correctness(arr):
        print("INSERTION SORT OK")
    else:
        print("INSERTION SORT FAIL")


if __name__ == "__main__":
    main()
