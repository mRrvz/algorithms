from random import randint

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1


def randomized_partition(arr, p, r):
    i = randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)


def randomized_selection(arr, i):

    def wrapper(arr, p, r, i):
        if p == r:
            return arr[p]

        q = randomized_partition(arr, p, r)
        k = q - p + 1
        
        if k == i:
            return arr[q]
        elif i < k:
            return wrapper(arr, p, q - 1, i)
        else:
            return wrapper(arr, q + 1, r, i - k )
        
    return wrapper(arr, 0, len(arr) - 1, i)


def main():
    arr = [0, 5, 6, 2, 3, 4, 15, 27]
    i = 5

    print("Result:", randomized_selection(arr, i))
    print("Expected:", sorted(arr)[i - 1])


if __name__ == "__main__":
    main()
