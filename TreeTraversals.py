def preorder(tree):
	'''root-left-right'''
	if tree:
		print(tree.get_root_val())
		preorder(tree.get_left_child())
		preorder(tree.get_right_child())

def postorder(tree):
	'''left-right-root'''
	if tree:
		postorder(tree.get_left_child())
		postorder(tree.get_right_child())
		print(tree.get_root_val())

def inorder(tree):
	'''left-root-right'''
	if tree:
		inorder(tree.get_left_child())
		print(tree.get_root_val())
		inorder(tree.get_right_child())