from avl import AVLTree 
class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.objects = AVLTree()  # List to store objects

    def add_object(self, obj):
        self.objects.root = self.objects.insert(self.objects.root, obj.id, obj)  # Add object to the list
        self.capacity -= obj.capacity  # Decrease bin capacity
        pass

    def remove_object(self, object_id):
        temp_obj = self.objects.find(self.objects.root, object_id)
        self.objects.root = self.objects.delete(self.objects.root, object_id, object_id) # remove object
        self.capacity += temp_obj.capacity  # Increase bin capacity

    def get_info(self):
        object_ids = self.in_order_traversal(self.objects.root)
        return self.capacity, object_ids  # Return remaining capacity

    def in_order_traversal(self, node):
        elements = []
        if node:
            elements += self.in_order_traversal(node.left)
            elements.append(node.info.id)    
        if node:
            elements += self.in_order_traversal(node.right)
        return elements
