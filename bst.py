class node:
	def __init__(self,val):
		self.p=None
		self.lchild=None
		self.rchild=None
		self.data=val
def binary_insert(root,node):
	if root is None:
		root = node
	else:
		if root.data>node.data:
			if root.lchild is None:
				root.lchild = node
			else:
				binary_insert(root.lchild,node)
		else:
			if root.rchild is None:
				root.rchild=node
			else:
				binary_insert(root.rchild,node)
		node.p=root
def in_order(root):
	if not root:
		return
	in_order(root.lchild)
	print (root.data)
	in_order(root.rchild)
def pre_order(root):
	if not root:
		return
	print(root.data)
	pre_order(root.lchild)
	pre_order(root.rchild)
def pre_order(root):
	if not root:
		return
	print(root.data)
	pre_order(root.lchild)
	pre_order(root.rchild)
def search(root,data):
	if (root==None):
		print("data not found")
	elif(data>root.data):
		search(root.rchild,data)
	elif(data<root.data):
		search(root.lchild,data)
	elif(data==root.data):
		print("found")


r=node(1)
binary_insert(r,node(7))
binary_insert(r,node(1))
binary_insert(r,node(5))
binary_insert(r,node(3))
in_order(r)
search(r,7)
