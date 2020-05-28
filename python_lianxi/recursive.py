'''
recursive
'''


def print_num(n):
	for i in range(1, n+1):
		print(i)
if __name__ == '__main__':
	print_num(10)

def print_num_recursive(n):
	if n > 0:
		print_num_recursive(n-1)
		print(n)

def print_num_recursive_reverserve(n):
	if n > 0:
		print(n)
		print_num_recursive_reverserve(n-1)


from collections import deque
class Stack(object):
	"""dtring for Stack"""
	def __init__(self):
		self.deque = deque()
	def push(self, value):
		return self.__deque.append(value)
	def pop(self):
		return self.__deque.pop()
	def is_empty(self):
		return len(self.__deque) == 0

	def print_num_use_stack(n):
		s = Stack()
		while n > 0:
			s.push(n)
			n -= 1

		while not s.is_empty():
			print(s.pop())
		