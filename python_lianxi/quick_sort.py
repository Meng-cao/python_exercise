'''
quicksort
'''
'''
def quicksort(array):
	size = len(array)
	if not array or size <2:
		return array
	pivot_index = 0
	pivot = array[pivot_index]

	less_part = [array[i] for i in range(size) if array[i] < pivot and pivot_index != i]
	great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_index != i]

	return quicksort(less_part) + [pivot] + quicksort(great_part)

def test_quicksort():
	import random
	seq = list(range(10))
	random.shuffle(seq)
	assert quicksort(seq) == sorted(seq)
	print(quicksort(seq))

test_quicksort()
'''
def quicksort_inplace(array, beg, end):
	if beg < end:
		pivot = partition(array, beg, end)
		quicksort_inplace(array, pivot, end)
		quicksort_inplace(array, beg, end-1)

def partition(array, beg, end):
		pivot_index = beg
		pivot = array[pivot_index]
		left = pivot_index + 1 #默认pivot_index = 0
		right = end - 1
		while True:
			while left <= right and array[left] <= pivot:
				left += 1
			while right >= left and array[right] >= pivot:
				right -= 1 
			if left > right:
				break
			else:
				array[left], array[right] = array[right], array[left]

		array[pivot_index], array[right] = array[right], array[pivot_index]
		return right # new pivot 

def test_partition():
	array = [1,2,6,3,7,9,4]
	print(partition(array, 0, len(array)))

test_partition()
