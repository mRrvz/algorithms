from random import randint
from utils import check_correctness


class Heap():
    def __init__(self, array, hsize):
        self.arr = array
        self.heap_size = hsize

        for i in range(self.get_hsize() // 2, -1, -1):
            self.max_heapify(i)


    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        largest = l if self.get_hsize() > l and self.get_key(l) > self.get_key(i) else i
        largest = r if self.get_hsize() > r and self.get_key(r) > self.get_key(largest) else largest

        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)


    def parent(self, i):
        return 2 // i + 1

    
    def right(self, i):
        return 2 * i + 2


    def left(self, i):
        return 2 * i + 1


    def get_array(self):
        return self.arr


    def get_hsize(self):
        return self.heap_size


    def set_array(self, array):
        self.arr = arr


    def set_hsize(self, hsize):
        self.heap_size = hsize


    def swap(self, i, j):
        self.arr[j], self.arr[i] = self.arr[i], self.arr[j]


    def get_key(self, i):
        return self.arr[i]


def heap_sort(arr):
    heap = Heap(arr, len(arr))

    for i in range(len(arr) - 1, 0, -1):
        heap.swap(i, 0)
        heap.set_hsize(heap.get_hsize() - 1)
        heap.max_heapify(0)

    return heap.get_array()


def main():
    arr = [randint(0, 10) for i in range(11)]

    if check_correctness(heap_sort(arr)):
        print("HEAP SORT IS OK")
    else:
        print("HEAP SORT FAIL")


if __name__ == "__main__":
    main()
    
