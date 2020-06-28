def parent(i):
    return 2 // i + 1


def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def max_heapify(arr, i):
    l = left(i)
    r = right(i)

    if len(arr) > l and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if len(arr) > r and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest)


def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        max_heapify(arr, i)


def main():
    #arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(arr)
    #max_heapify(arr, 1)
    print(arr)


if __name__ == "__main__":
    main()
    
