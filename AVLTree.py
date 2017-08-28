from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode

class AVLTree(BinarySearchTree):

    def __init__(self):
        super().__init__()

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.has_left_child())
            else:
                currentNode.left_child = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.left_child)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.right_child)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return

        # Base case 1
        if node.parent != None:
            if node.is_left_child():
                node.parent.balanceFactor += 1
            elif node.is_right_child():
                node.parent.balanceFactor -= 1

            # Base case 2
            # Once a subtree has a balance factor of zero, then the balance of its ancestor 
            # nodes does not change.
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.right_child.balanceFactor > 0:
                self.rotateRight(node.right_child)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        else:
            if node.left_child.balanceFactor < 0:
                self.rotateLeft(node.left_child)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.right_child
        rotRoot.right_child = newRoot.left_child
        if newRoot.left_child != None:
            newRoot.left_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_left_child():
                rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.right_child = newRoot
        newRoot.left_child = rotRoot
        rotRoot.parent = newRoot

        # You can get the formula via calculating
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.left_child
        rotRoot.left_child = newRoot.right_child
        if newRoot.right_child != None:
            newRoot.right_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_left_child():
                rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.right_child = newRoot
        newRoot.right_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

    def updateBalance_delete(self, node):
        if node.parent != None:
            if node.is_left_child():
                node.parent.balanceFactor -= 1
            elif node.is_right_child():
                node.parent.balanceFactor += 1

            if node.parent.parent != None:
                self.updateBalance_delete(node.parent)

        if node.parent.balanceFactor < -1 or node.parent.balanceFactor >1:
            self.rebalance(node.parent)
            return

    def remove(self, node_to_remove):
        if node_to_remove.is_leaf():
            self.updateBalance_delete(node_to_remove)
            if node_to_remove.is_left_child():
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None
        elif node_to_remove.has_both_children():
            succ = node_to_remove.find_successor()
            self.updateBalance_delete(succ)
            succ.splice_out()
            node_to_remove.key = succ.key
            node_to_remove.payload = succ.payload
        else:
            if node_to_remove.has_left_child():
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                    self.updateBalance_delete(node_to_remove)
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.left_child
                    self.updateBalance_delete(node_to_remove)
                # If node_to_remove is a root node
                else:
                    node_to_remove.replace_node_data(node_to_remove.left_child.key,
                                                     node_to_remove.left_child.payload,
                                                     node_to_remove.left_child.left_child,
                                                     node_to_remove.left_child.right_child)
                    self.updateBalance_delete(node_to_remove.left_child)
            else:
                if current_node.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                    self.updateBalance_delete(node_to_remove)
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                    self.updateBalance_delete(node_to_remove)
                # If node_to_remove is a root node
                else:
                    node_to_remove.replace_node_data(node_to_remove.right_child.key,
                                                     node_to_remove.right_child.payload,
                                                     node_to_remove.right_child.left_child,
                                                     node_to_remove.right_child.right_child)
                    self.updateBalance_delete(node_to_remove.right_child)

if __name__ == '__main__':
    my_tree = AVLTree()
    my_tree[8] = 'true root'
    my_tree[6] = 'root'
    my_tree[3] = 'red'
    my_tree[9] = 'blue'
    my_tree[4] = 'yellow'
    my_tree[2] = 'at'

    '''
    print(my_tree.root.key)
    print(my_tree.root.left_child.key)
    print(my_tree.root.right_child.key)
    print(my_tree.root.left_child.left_child.key)
    print(my_tree.root.left_child.right_child.key)
    print(my_tree.root.right_child.right_child.key)
    '''

    #print(my_tree.root.right_child.balanceFactor)

    my_tree.delete(9)

    '''print(my_tree.root.key)
    print(my_tree.root.balanceFactor)
    print(my_tree.root.right_child.key)
    print(my_tree.root.right_child.balanceFactor)
    '''

    my_tree.delete(8)

    print(my_tree.root.key)
    print(my_tree.root.balanceFactor)
    print(my_tree.root.left_child.key)
    print(my_tree.root.right_child.key)
    print(my_tree.root.right_child.left_child.key)