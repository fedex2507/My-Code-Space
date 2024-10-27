from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins_by_capacity = AVLTree()
        self.bins_by_id = AVLTree()
        self.objects_by_id = AVLTree()

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.bins_by_capacity.root = self.bins_by_capacity.insert(self.bins_by_capacity.root, new_bin.capacity ,new_bin)
        self.bins_by_id.root = self.bins_by_id.insert(self.bins_by_id.root, new_bin.id ,new_bin)

    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
        best_bin = None
        if obj.color == 1:
            best_bin = self.Compact_fit_Blue(self.bins_by_capacity.root, obj, best_bin)
        elif obj.color == 2:
            best_bin = self.Compact_fit_Yellow(self.bins_by_capacity.root, obj, best_bin)
        else:
            if obj.color == 3:
                best_bin = self.Largest_fit_Red(self.bins_by_capacity.root, obj, best_bin)
            else:
                best_bin = self.Largest_fit_Green(self.bins_by_capacity.root, obj, best_bin)

        # Final check to see if we found a suitable bin
        # Remove and reinsert the bin in the AVL tree to maintain balance
        if best_bin == None:
            raise NoBinFoundException()

        self.bins_by_capacity.root = self.bins_by_capacity.delete(self.bins_by_capacity.root, best_bin.capacity, best_bin.id)
        best_bin.add_object(obj)
        self.bins_by_capacity.root = self.bins_by_capacity.insert(self.bins_by_capacity.root, best_bin.capacity, best_bin)
        obj.bin = best_bin  # Assign the bin ID to the object
        self.objects_by_id.root = self.objects_by_id.insert(self.objects_by_id.root, obj.id, obj)
        pass
        
    def delete_object(self, object_id):
        temp_obj = self.objects_by_id.find(self.objects_by_id.root, object_id) # Find object
        if temp_obj is None:
            return None
        temp_bin = temp_obj.bin # Object contained in bin
        self.objects_by_id.root = self.objects_by_id.delete(self.objects_by_id.root, object_id, object_id) # Delete object from Object Tree
        self.bins_by_capacity.root = self.bins_by_capacity.delete(self.bins_by_capacity.root, temp_bin.capacity, temp_bin.id)
        temp_bin.remove_object(object_id)
        self.bins_by_capacity.root = self.bins_by_capacity.insert(self.bins_by_capacity.root, temp_bin.capacity, temp_bin)

    def bin_info(self, bin_id):
        bin_node = self.bins_by_id.find(self.bins_by_id.root, bin_id)
        if bin_node:
            return bin_node.get_info()
        return None

    def object_info(self, object_id):
        temp_obj = self.objects_by_id.find(self.objects_by_id.root, object_id)
        if temp_obj is None:
            return None
        temp_bin = temp_obj.bin
        return temp_bin.id
    
    def Compact_fit_Yellow(self,node, obj, best_bin):
        # Finding the best bin based on color
        def find_compact_fit(node, obj):
            nonlocal best_bin
            if not node:
                return
            find_compact_fit(node.left, obj)
            if best_bin is None and obj.capacity <= node.key:
                best_bin = node
            elif best_bin is not None:
                if (best_bin.key == node.key and node.info.id > best_bin.info.id):
                    best_bin = node
            if best_bin is not None and best_bin.key < node.key:
                return
            find_compact_fit(node.right, obj)
        
        find_compact_fit(node, obj)

        if best_bin is not None:
            return best_bin.info
        else:
            return None

    def Compact_fit_Blue(self, node, obj, best_bin):
        def find_compact_fit(node, obj):
            nonlocal best_bin
            if not node:
                return
            find_compact_fit(node.left, obj)
            if best_bin is None and obj.capacity <= node.key:
                best_bin = node
            elif best_bin is not None:
                if (best_bin.key == node.key and node.info.id < best_bin.info.id):
                    best_bin = node
            if best_bin is not None and best_bin.key < node.key:
                return
            find_compact_fit(node.right, obj)
            
        find_compact_fit(node, obj)

        if best_bin is not None:
            return best_bin.info
        else:
            return None

    def Largest_fit_Green(self, node, obj, best_bin):
        # Finding the best bin based on color
        def largest_fit(node, obj):
            nonlocal best_bin
            if not node:
                return
            largest_fit(node.right, obj)
            if best_bin is None and obj.capacity <= node.key:
                best_bin = node
            if best_bin is not None and best_bin.key > node.key:
                return
            elif best_bin is not None:
                if (best_bin.key == node.key and node.info.id > best_bin.info.id):
                    best_bin = node
            largest_fit(node.left, obj)
            
        largest_fit(node, obj)
    
        if best_bin is not None:
            return best_bin.info
        else:
            return None

    def Largest_fit_Red(self, node, obj, best_bin):
        # Finding the best bin based on color
        def largest_fit(node, obj):
            nonlocal best_bin
            if not node:
                return
            largest_fit(node.right, obj)
            if best_bin is None and obj.capacity <= node.key:
                best_bin = node
            if best_bin is not None and best_bin.key > node.key:
                return
            elif best_bin is not None:
                if (best_bin.key == node.key and node.info.id < best_bin.info.id):
                    best_bin = node
            largest_fit(node.left, obj)
            
        largest_fit(node, obj)
    
        if best_bin is not None:
            return best_bin.info
        else:
            return None
            













    
    