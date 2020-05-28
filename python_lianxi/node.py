"""
Node 链表
"""
class Node(object):
	"""docstring for Node"""
	def __init__(self, value, next = None):
		self.value = value
		self.next = next 
class LinkedList(object):
	#链接表ADT [root]->[node0]->[node1]->[node2]
	def __init__(self, arg):
		super(LinkedList, self).__init__()
		self.arg = arg
'''
双链表：节点双箭头，既保存了上一个节点的指针，又保存了指向下一个节点的指针

'''
