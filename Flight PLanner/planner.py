class Node:
    __slots__ = ['city', 'previous', 'flight']
    def __init__(self, city, previous=None, flight=None):
        self.city = city  # Current city
        self.previous = previous  # The previous node (for backtracking)
        self.flight = flight  # The flight taken to reach this city (for backtracking)

class Node_for_queue:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def enqueue(self, value):
        new_node = Node_for_queue(value)    
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Link the new node to the rear
            self.rear = new_node       # Update the rear pointer

    def dequeue(self):
        value = self.front.value  # Retrieve the value at the front
        self.front = self.front.next  # Move the front pointer forward
        if self.front is None:  # If the queue becomes empty, update rear to None
            self.rear = None
        return value

    def is_empty(self):
        return self.front is None

class Heap: 
    def __init__(self, comparison_function):
        self.cmp = comparison_function  # Custom comparison function
        self.heap = [] 

    def is_empty(self):
        return len(self.heap)== 0

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        if len(self.heap) == 0:
            return None
        top = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify_down(0)
        return top
    
    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.cmp(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    
    def heapify_down(self, index):
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

class Planner:
    def __init__(self, flights):
        self.flights = flights
        self.max_city = max(max(flight.start_city for flight in flights), max(flight.end_city for flight in flights))
        self.adjacency_list = self.build_adjacency_list()

    def build_adjacency_list(self):
        adj_list = [[] for _ in range(self.max_city+2)]
        for flight in self.flights:
            adj_list[flight.start_city].append(flight)
        return adj_list

    def is_valid(self, flight, arrival_time, t1, t2):
        """Check if the flight can be taken within the time window and layover constraints."""
        return flight.departure_time >= arrival_time + 20 and flight.arrival_time <= t2

    def _reconstruct_path(self, final_node):
        """Backtrack from the final node to construct the path."""
        path = []
        node = final_node

        while node and node.flight:           # Traverse back through the nodes using the previous attribute
            path.append(node.flight)          # Append the flight taken to reach this node
            node = node.previous              # Move to the previous node

        path.reverse()                        # Reverse to get the path from start_city to end_city
        return path

    class Vault:
        def __init__(self, city, cost, arrival_time, previous = None, flight=None):
            self.city = city
            self.cost = cost
            self.arrival_time = arrival_time
            self.previous = previous
            self.flight = flight

    def _reconstruct_path_array(self, prev_flight, end_city, start_city):
        path = []
        curr_city = end_city
        while curr_city != start_city and prev_flight[curr_city]:
            path.append(prev_flight[curr_city])
            curr_city = prev_flight[curr_city].start_city
        path.reverse()
        return path

    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city or t1 > t2:
            return []
            
        best_arrival = [(float('inf'), float('inf'))] * (self.max_city + 2)
        best_arrival[start_city] = (t1 - 20, 0)
        prev_flight = [None] * (len(self.flights) + 2)

        queue = Queue()
        queue.enqueue((start_city, t1 - 20, 0))

        while not queue.is_empty():
            city, arrival, flight_count = queue.dequeue()

            if (arrival, flight_count) != best_arrival[city]:
                continue

            for flight in self.adjacency_list[city]:
                if (flight.departure_time >= t1 and flight.arrival_time <= t2 and flight.departure_time >= arrival + 20):
                    new_arrival = flight.arrival_time
                    new_count = flight_count + 1

                    curr_arrival, curr_count = best_arrival[flight.end_city]
                    if (new_count < curr_count or (new_count == curr_count and new_arrival < curr_arrival)):
                        best_arrival[flight.end_city] = (new_arrival, new_count)
                        prev_flight[flight.end_city] = flight
                        queue.enqueue((flight.end_city, new_arrival, new_count))

        return self._reconstruct_path_array(prev_flight, end_city, start_city)

    def cheapest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city or t1 > t2:
            return []

        # Initialize priority queue with (cost, arrival_time, start_node)
        priority_queue = Heap(self.compare)
        start_node = Node(start_city)  # Starting node with cost = 0 and adjusted start time
        priority_queue.insert((0, t1 - 20, start_node))  # Push (cost, arrival_time, node)
        # Visited dictionary to track minimum cost and earliest arrival time for each city
        minimal_cost = float("inf") # min_cost
        minimal_arrival_time = float("inf")  # min_arrival_time
        final_node = None
        passed = [False]*(len(self.flights)+1)

        while not priority_queue.is_empty():
            cost, arrival_time, node = priority_queue.extract()
            curr_city = node.city

            # If we've reached the destination, update if it's the cheapest route
            if curr_city == end_city:
                if cost < minimal_cost:
                    final_node = node
                    minimal_cost = cost
                break
 
            # Explore neighboring flights
            for flight in self.adjacency_list[curr_city]:
                if passed[flight.flight_no]:
                    continue
                # Calculate the new cost for this flight
                new_cost = cost + flight.fare
                if self.is_valid(flight, arrival_time, t1, t2):                                   
                    new_node = Node(flight.end_city, previous=node, flight=flight)
                    priority_queue.insert((new_cost, flight.arrival_time, new_node))
                    passed[flight.flight_no] = True

        # Backtrack to get the route from the final node
        return self._reconstruct_path(final_node) if final_node else []

    def compare(self, x, y):
        if x[0] == y[0]:
            return x[1] < y[1]
        return x[0] < y[0]

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        if start_city == end_city or t1 > t2:
            return []

        # Initialize priority queue with (cost, fare, arrival_time, node)
        priority_queue = Heap(self.compare)  # Min heap based on cost
        start_node = Node(start_city)  # Starting node with cost = 0 and adjusted start time
        priority_queue.insert((0, 0, t1 - 20, start_node))  # (cost, total_fare, arrival_time, node)

        # Visited dictionary to track minimum cost and fare for each city
        minimal_cost = float("inf")
        minimal_fare = float("inf")
        final_node = None
        passed = [False] * (len(self.flights) + 1)

        while not priority_queue.is_empty():
            cost, total_fare, arrival_time, node = priority_queue.extract()
            curr_city = node.city

            # If we reach the destination city, update the final_node if this route is cheaper
            if curr_city == end_city:
                if cost < minimal_cost:
                    final_node = node
                    minimal_cost = cost
                break

            # Explore neighboring flights
            for flight in self.adjacency_list[curr_city]:
                if passed[flight.flight_no]:
                    continue
                new_cost = cost + 1
                new_fare = total_fare + flight.fare

                # Check if this route is valid and cheaper
                if self.is_valid(flight, arrival_time, t1, t2):
                    new_node = Node(flight.end_city, previous=node, flight=flight)
                    priority_queue.insert((new_cost, new_fare, flight.arrival_time, new_node))
                    passed[flight.flight_no] = True

        # Backtrack to get the route from the final node
        return self._reconstruct_path(final_node) if final_node else []