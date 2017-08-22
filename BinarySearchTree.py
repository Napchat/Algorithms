from TreeNode import TreeNode

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val,
                    parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val,
                    parent=current_node)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node_to_remove):
        if node_to_remove.is_leaf():
            if node_to_remove == node_to_remove.parent.left_child:
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None
        elif node_to_remove.has_both_children():
            succ = node_to_remove.find_successor()
            succ.splice_out()
            node_to_remove.key = succ.key
            node_to_remove.payload = succ.payload
        else:
            if node_to_remove.has_left_child():
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.left_child
                # If node_to_remove is a root node
                else:
                    node_to_remove.replace_node_data(node_to_remove.left_child.key,
                                                     node_to_remove.left_child.payload,
                                                     node_to_remove.left_child.left_child,
                                                     node_to_remove.left_child.right_child)
            else:
                if current_node.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                # If node_to_remove is a root node
                else:
                    node_to_remove.replace_node_data(node_to_remove.right_child.key,
                                                     node_to_remove.right_child.payload,
                                                     node_to_remove.right_child.left_child,
                                                     node_to_remove.right_child.right_child)

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, k, v):
        '''This method defines the `[]` operator
        It allows us to write statements like `my_zip_tree['Plymouth'] = 55446`
        '''
        self.put(k, v)

    def __contatins__(self, key):
        '''__contains__ overloads the `in` operator'''
        if self._get(key, self.root):
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree[8] = 'true root'
    my_tree[6] = 'root'
    my_tree[3] = 'red'
    my_tree[9] = 'blue'
    my_tree[4] = 'yellow'
    my_tree[2] = 'at'

    my_tree.delete(8)
    print(my_tree.root.key)