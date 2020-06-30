from random import randint
from utils import check_correctness


def counting_sort(arr):
    arr_copy = [0 for x in range(len(arr))]
    sorted_arr = [0 for x in range(len(arr))]

    for key in arr:
        arr_copy[key - 1] += 1

    for i in range(1, len(arr)):
        arr_copy[i] += arr_copy[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[arr_copy[arr[i] - 1] - 1] = arr[i]
        arr_copy[arr[i] - 1] -= 1

    return sorted_arr


def main():
    print(arr := [randint(1, 10) for x in range(10)])

    if check_correctness(arr := counting_sort(arr)):
        print("COUNTING SORT IS OK")
    else:
        print("COUNTING SORT FAIL")


if __name__ ==  "__main__":
    main()

