import heap

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Initializes the crewmate with an empty heap for treasures and a load counter.
        '''
        # Sorted based on arrival time
        self.treasures = []
        self.size = 0  # Total remaining size of treasures
        self.last_upadted_time = 0
        self.prev_index = 0

    def add_treasure(self, treasure):
        '''
        Adds a treasure to the crewmate's heap and updates the load.
        '''
        self.treasures.append(treasure)
        self.size = treasure.size + max(treasure.arrival_time,self.size)

    def more_process_treasure(self, completion_list, treasures_sort, time, time_diff):
        time += treasures_sort.heap[0].size
        time_diff -= treasures_sort.heap[0].size
        self.size -= treasures_sort.heap[0].size
        treasures_sort.heap[0].size = 0
        treasures_sort.heap[0].completion_time = time
        top_treasure = treasures_sort.extract()
        completion_list.append(top_treasure)

        return time, time_diff
        
    def pre_process_treasure(self, completion_list, j, treasures_sort, time):
        for i in range(j+1,len(self.treasures)):
            if self.treasures[i].size == 0:
                completion_list.append(self.treasures[i])
                continue
            if self.prev_index == i :
                time = self.last_upadted_time
            time_diff = self.treasures[i].arrival_time - time
            while time_diff > 0 :
                if treasures_sort.top() is None:
                    break
                if time_diff < treasures_sort.heap[0].size:
                    time += time_diff
                    self.size -= time_diff # crewmate updated load
                    treasures_sort.heap[0].size -= time_diff
                    break
                else:
                    time, time_diff = self.more_process_treasure(completion_list,treasures_sort,time,time_diff)             
            time = self.treasures[i].arrival_time
            treasures_sort.insert(self.treasures[i])

        return time

    def process_treasure(self, completion_list):
        '''
        Processes the treasure with the highest priority (smallest size in this case) and updates load.
        '''
        def compare(x, y):
            if x.size + x.arrival_time == y.size + y.arrival_time:
                return x.id < y.id
            return (x.size + x.arrival_time) < (y.size + y.arrival_time)
        
        treasures_sort = heap.Heap(lambda x,y: compare(x,y) , [])
        
        j = 0 
        while j < len(self.treasures):
            if self.treasures[j].size > 0:
                treasures_sort.insert(self.treasures[j])
                time = self.treasures[j].arrival_time
                break
            completion_list.append(self.treasures[j])
            j += 1

        if j == len(self.treasures):
            return 

        time = self.pre_process_treasure(completion_list, j, treasures_sort, time)

        # Remaining treasures
        if treasures_sort is None:
            return

        self.last_upadted_time = time
        self.prev_index = len(self.treasures)-1

        i = 0
        while i < len(treasures_sort.heap):
            time += treasures_sort.heap[i].size
            treasures_sort.heap[i].completion_time = time
            completion_list.append(treasures_sort.heap[i])
            i += 1

        return
