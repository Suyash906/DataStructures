def partition(array, start, end):
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		if array[left] > array[pivot] and array[pivot] > array[right]:
			array[left], array[right] = array[right], array[left]
		if array[left] <= array[pivot]:
			left += 1
		if array[pivot] <= array[right]:
			right -= 1
	array[pivot], array[right] = array[right], array[pivot]
	return right

def quickSortUtil(array, left, right):
	## base
	if left >= right:
		return
	
	## body
	pivot = partition(array, left, right)
	# return
	if pivot - 1 - left < right - (pivot + 1):
		quickSortUtil(array, left, pivot - 1)
		quickSortUtil(array, pivot + 1, right)
	else:
		quickSortUtil(array, pivot + 1, right)
		quickSortUtil(array, left, pivot - 1)
		
def quickSort(array):
    # Write your code here.
    quickSortUtil(array, 0, len(array)-1)
    return array


def main():
    array = [8, 5, 2, 9, 5, 6, 3]
    res = quickSort(array)
    print('Input = ',  array)
    print('Output = ', res)

if __name__ == '__main__':
    main()
