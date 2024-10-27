from node import Node

def comp_1(node_1, node_2):
    return node_1 - node_2 

class AVLTree:
    def __init__(self, compare_function = comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        if x is None:  # Check if x is None before proceeding
            return y  # Return the current node if rotation is not possible
        
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        if y is None:  # Check if y is None before proceeding
            return x  # Return the current node if rotation is not possible
        
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y


    def insert(self, node, key, bin_info):    
        if not node:
            self.size += 1 # Update size
            return Node(key, bin_info)
        if self.comparator(key, node.key) < 0:
            node.left = self.insert(node.left, key, bin_info)
        elif self.comparator(key,node.key) == 0:
            if self.comparator(bin_info.id,node.info.id) < 0:
                node.left = self.insert(node.left, key, bin_info)
            else:
                node.right = self.insert(node.right, key, bin_info)
        else:
            node.right = self.insert(node.right, key, bin_info)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.comparator(bin_info.id, node.left.key) < 0:
            return self.right_rotate(node)
        if balance < -1 and self.comparator(key, node.right.key) > 0:
            return self.left_rotate(node)
        if balance > 1 and self.comparator(key, node.left.key) > 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.comparator(key, node.right.key) < 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, node, key, bin_id):
        self.size -= 1 # Update size
        node = self.delete_now(node, key, bin_id)
        return node

    def delete_now(self, node, key, bin_id):    
        if not node:
            return node

        if self.comparator(key, node.key) < 0:
            node.left = self.delete(node.left, key, bin_id)
        elif key > node.key:
            node.right = self.delete(node.right, key, bin_id)
        else:
            if self.comparator(bin_id, node.info.id) < 0:
                node.left = self.delete(node.left, key, bin_id)
            elif self.comparator(bin_id, node.info.id) > 0:
                node.right = self.delete(node.right, key, bin_id)  
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.min_value_node(node.right)
                node.key, node.info = temp.key, temp.info
                node.right = self.delete(node.right, temp.key, temp.info.id)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def find(self, node, key):
        if not node:
            return None
        if self.comparator(key, node.key) == 0:
            return node.info
        elif self.comparator(key, node.key) < 0:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def find_two_parameter(self, node, key, arg_id):
        if not node:
            return None
        if key == node.key:
            if self.comparator(arg_id, node.info.id) < 0:
                return self.find_two_parameter(node.left, key, arg_id)
            elif self.comparator(arg_id, node.info.id) > 0:
                return self.find_two_parameter(node.right, key, arg_id)
            else:
                return node
        elif self.comparator(key, node.key) < 0:
            return self.find_two_parameter(node.left, key, arg_id)
        else:
            return self.find_two_parameter(node.right, key, arg_id)

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)
