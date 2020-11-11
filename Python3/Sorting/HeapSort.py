def left(array, end_index, i):
    left_index = 2 * i + 1
    if left_index > end_index: return -1
    return left_index


def right(array, end_index, i):
    right_index = 2 * i + 2
    if right_index > end_index: return -1
    return right_index


def parent(array, i):
    if i == 0: return -1
    return (i - 1) // 2


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def siftDown(array, end_index, i):
    max_index = i
    left_index = left(array, end_index, i)
    if -1 != left_index and array[left_index] > array[max_index]:
        max_index = left_index

    right_index = right(array, end_index, i)
    if -1 != right_index and array[right_index] > array[max_index]:
        max_index = right_index

    if max_index != -1 and max_index != i:
        swap(array, i, max_index)
        siftDown(array, end_index, max_index)


def buildMaxHeap(array, end_index):
    n = len(array)
    for i in range(((end_index + 1) // 2) - 1, -1, -1):
        siftDown(array, end_index, i)


def heapSort(array):
    n = len(array)
    buildMaxHeap(array, n - 1)

    index = n - 1
    while index > 0:
        swap(array, 0, index)
        index -= 1
        buildMaxHeap(array, index)
    return array
