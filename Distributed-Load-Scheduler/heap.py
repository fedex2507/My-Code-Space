class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Initializes a heap with a comparison function and builds the heap.
        
        Args:
        - comparison_function: A function that takes two elements and returns True if the first element should be placed higher in the heap, False otherwise.
        - init_array: An initial array to build the heap from.
        '''
        self.cmp = comparison_function  # Custom comparison function
        self.heap = init_array[:]        
        self.build_heap()

    def build_heap(self):
        '''
        Builds the heap from the initial array.
        '''
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify_down(i)
    
    def insert(self, value):
        '''
        Inserts a value into the heap and maintains the heap property.
        
        Args:
        - value: The value to be inserted into the heap.
        '''
        self.heap.append(value)
        # self.heap_size += 1
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        '''
        Extracts the top element of the heap and maintains the heap property.
        
        Returns:
        - The top element of the heap, or None if the heap is empty.
        '''
        if len(self.heap) == 0:
            return None
        top = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify_down(0)
        return top
    
    def top(self):
        '''
        Returns the top element of the heap without removing it.
        
        Returns:
        - The top element of the heap, or None if the heap is empty.
        '''
        return self.heap[0] if len(self.heap) > 0 else None
    
    def heapify_up(self, index):
        '''
        Bubbles up the element at the given index to maintain the heap property.
        
        Args:
        - index: The index of the element to be bubbled up.
        '''
        parent = (index - 1) // 2
        if index > 0 and self.cmp(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        '''
        Bubbles down the element at the given index to maintain the heap property.
        
        Args:
        - index: The index of the element to be bubbled down.
        '''
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        
        if left < len(self.heap) and self.cmp(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.cmp(self.heap[right], self.heap[smallest]):
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
