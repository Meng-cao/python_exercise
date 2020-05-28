"""
array 
"""

from array import array

class Array(object):
	"""docstring for Array"""
	def __init__(self, size = 32):
		self.size = size
		self._items = [None] * size
	def __getitem__(self, index):
		return self._items[index]
	