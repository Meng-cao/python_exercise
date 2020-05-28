'''
bubble
'''
import random
'''
def bubble_sort(seq):
	for i in range(len(seq)-1):	
		for j in range(len(seq)-1-i):
			if seq[j] > seq[j+1]:
				seq[j],seq[j+1] = seq[j+1],seq[j]
	return seq


def select_sort(seq):
	for i in range(len(seq)-1):
		min_idx = i 
		for j in range(i+1, len(seq)):
			if seq[j] < seq[min_idx]:
				min_idx = j
		if min_idx != i:
			seq[i], seq[min_idx] = seq[min_idx],seq[i]
	return seq
'''
def insertion_sort(seq):
	for i in range(1,len(seq)):
		value = seq[i]
		pos = i
		while pos > 0 and value < seq[pos-1]:
			seq[pos] = seq[pos-1]
			pos -= 1
		seq[pos] = value
	return seq 

def test_bubble_sort():
	seq = list(range(10)) # python3返回迭代器 用list强转
	random.shuffle(seq)
	insertion_sort(seq)
	assert seq == sorted(seq) #判断一下是不是排好了
	print(insertion_sort(seq)) 

test_bubble_sort()
