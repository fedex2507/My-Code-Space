from typing import List, Dict, Tuple
from queue import Queue
import random
import math

class CircuitElement:
    def __init__(self, identifier, width, height, connection_points, latency):
        self.identifier = identifier
        self.width = width
        self.height = height
        self.connection_points = connection_points
        self.latency = latency
        self.position = (0, 0)
        self.incoming_connections = 0

    def connect(self, connection):
        if connection.source == self.identifier:
            if self.connection_points[f'{connection.source}.{connection.source_point}'].position[0] == 0:
                self.incoming_connections += 1
        if connection.destination == self.identifier:
            if self.connection_points[f'{connection.destination}.{connection.dest_point}'].position[0] == 0:
                self.incoming_connections += 1

    def __str__(self):
        return f"[{self.identifier} {self.width} {self.height} {self.latency} {self.connection_points}]"

class Connection:
    def __init__(self, source: str, source_point: str, destination: str, dest_point: str):
        self.source = source
        self.source_point = source_point
        self.destination = destination
        self.dest_point = dest_point

class ConnectionPoint:
    def __init__(self, element: str, point: str, position: Tuple[int, int] = (0, 0)):
        self.element = element
        self.point = point
        self.connections = []
        self.position = position
        self.absolute_position = (0, 0)

    def connect(self, connection: Connection):
        self.connections.append(connection)

def primay_input(connection_points_dict):
    entry_points = []
    for point_id, point in connection_points_dict.items():
        if not point.connections and point.position[0] == 0:
            entry_points.append(point_id.split('.')[0])
    entry_points = list(set(entry_points))
    return entry_points

def primary_output(connection_points_dict):
    exit_points = []
    for point_id, point in connection_points_dict.items():
        if not point.connections and point.position[0] != 0:
            exit_points.append(point_id.split('.')[0])
    exit_points = list(set(exit_points))
    return exit_points

def update_final_postsn(connection_points_dict, elements_dict):
    connection_points_dict_ = connection_points_dict.copy()
    elements_dict_ = elements_dict.copy()
    for point_id, point in connection_points_dict_.items():
        element = elements_dict_[point.element]
        point.absolute_position = (
            element.position[0] + element.connection_points[f'{point.element}.{point.point}'].position[0],
            element.position[1] + element.connection_points[f'{point.element}.{point.point}'].position[1]
        )
    return connection_points_dict_, elements_dict_

def cord_max(coords):
    i = len(coords)-1
    if i < 0:
        return None
    max_coord = coords[0]
    while i>=0:
        if max_coord < coords[i]:
            max_coord = coords[i]
        i -= 1
    return max_coord

def cord_min(coords):
    i = len(coords)-1
    if i < 0:
        return None

    min_coord = coords[0]
    while i>=0:
        if min_coord > coords[i]:
            min_coord = coords[i]
        i -= 1
    return min_coord
def _more_critical_delay(elements_dict, connection_points_dict, connection_delay,traversal_queue,processed_connections,delay_map):
    while not traversal_queue.empty():
        element_id = traversal_queue.get()
        element = elements_dict[element_id]
        for point_id, point in element.connection_points.items():
            if point.position[0] == 0:
                continue
            next_points = []
            for connection in point.connections:
                if connection.source == element_id:
                    next_points.append(f'{connection.destination}.{connection.dest_point}')
                else:
                    next_points.append(f'{connection.source}.{connection.source_point}')
            length = measure_connection_length(connection_points_dict, connection_points_dict[point_id])
            for next_point in next_points:
                next_element = next_point.split('.')[0]
                processed_connections[next_element] += 1
                if delay_map[next_element] < delay_map[element_id] + element.latency + connection_delay * length:
                    delay_map[next_element] = delay_map[element_id] + element.latency + connection_delay * length
                if processed_connections[next_element] == elements_dict[next_element].incoming_connections:
                    traversal_queue.put(next_element)
                    
def measure_connection_length(connection_points_dict, point):
    x_coords = [point.absolute_position[0]]
    y_coords = [point.absolute_position[1]]
    for connection in point.connections:
        if connection.source == point.element:
            next_point = connection_points_dict[f'{connection.destination}.{connection.dest_point}']
        else:
            next_point = connection_points_dict[f'{connection.source}.{connection.source_point}']
        x_coords.extend([next_point.absolute_position[0]])
        y_coords.extend([next_point.absolute_position[1]])

    return max(cord_max(x_coords) - cord_min(x_coords), cord_max(y_coords) - cord_min(y_coords))

def compute_critical_delay(elements, elements_dict, connection_points_dict, connection_delay) -> int:
    traversal_queue = Queue()
    delay_map = {element.identifier: 0 for element in elements}
    processed_connections = {element.identifier: 0 for element in elements}
    connection_points_dict, elements_dict = update_final_postsn(connection_points_dict, elements_dict)
    for element in primay_input(connection_points_dict):
        traversal_queue.put(element)
    _more_critical_delay(elements_dict, connection_points_dict, connection_delay,traversal_queue,processed_connections,delay_map)
    max_delay = 0
    for element in primary_output(connection_points_dict):
        max_delay = max(max_delay, delay_map[element] + elements_dict[element].latency)
    return max_delay

def get_single_entry_point(element, connection_points_dict):
    for point_id, point in connection_points_dict.items():
        if point.element == element and not point.connections and point.position[0] == 0:
            return point_id
    return None

def get_single_exit_point(element, connection_points_dict):
    for point_id, point in connection_points_dict.items():
        if point.element == element and not point.connections and point.position[0] != 0:
            return point_id
    return None

def _more_critical_path(elements_dict, connection_points_dict, connection_delay,traversal_queue,processed_connections,delay_map,path_map):
    while not traversal_queue.empty():
        element_id = traversal_queue.get()
        element = elements_dict[element_id]
        for point_id, point in element.connection_points.items():
            if point.position[0] == 0:
                continue
            next_points = []
            for connection in point.connections:
                if connection.source == element_id:
                    next_points.append(f'{connection.destination}.{connection.dest_point}')
                else:
                    next_points.append(f'{connection.source}.{connection.source_point}')
            length = measure_connection_length(connection_points_dict, connection_points_dict[point_id])
            for next_point in next_points:
                next_element = next_point.split('.')[0]
                processed_connections[next_element] += 1
                if delay_map[next_element] < delay_map[element_id] + element.latency + connection_delay * length:
                    delay_map[next_element] = delay_map[element_id] + element.latency + connection_delay * length
                    path_map[next_element] = path_map[element_id] + [point_id] + [next_point]
                if processed_connections[next_element] == elements_dict[next_element].incoming_connections:
                    traversal_queue.put(next_element)

def identify_critical_path(elements, elements_dict, connection_points_dict, connection_delay):
    traversal_queue = Queue()
    for element in primay_input(connection_points_dict):
        traversal_queue.put(element)
    delay_map = {element.identifier: 0 for element in elements}
    path_map = {element.identifier: [] for element in elements}

    for element in primay_input(connection_points_dict):
        path_map[element] = [get_single_entry_point(element, connection_points_dict)]
    processed_connections = {element.identifier: 0 for element in elements}
    update_final_postsn(connection_points_dict, elements_dict)
    _more_critical_path(elements_dict, connection_points_dict, connection_delay,traversal_queue,processed_connections,delay_map,path_map)
    max_delay = 0
    critical_path = []
    for element in primary_output(connection_points_dict):
        if max_delay < delay_map[element] + elements_dict[element].latency:
            max_delay = delay_map[element] + elements_dict[element].latency
            critical_path = path_map[element] + [get_single_exit_point(element, connection_points_dict)]
    return critical_path

def check_for_overlap(elements_dict) -> bool:
    return any(
        list(elements_dict.values())[i].position[0] < list(elements_dict.values())[j].position[0] + list(elements_dict.values())[j].width and
        list(elements_dict.values())[i].position[0] + list(elements_dict.values())[i].width > list(elements_dict.values())[j].position[0] and
        list(elements_dict.values())[i].position[1] < list(elements_dict.values())[j].position[1] + list(elements_dict.values())[j].height and
        list(elements_dict.values())[i].position[1] + list(elements_dict.values())[i].height > list(elements_dict.values())[j].position[1]
        for i in range(len(list(elements_dict.values())))
        for j in range(i + 1, len(list(elements_dict.values())))
    )

def genarate_neighbour_all(elements_dict, max_x, max_y):
    new_elements = {e.identifier: CircuitElement(e.identifier, e.width, e.height, e.connection_points, e.latency) for e in elements_dict.values()}
    for e, old_e in zip(new_elements.values(), elements_dict.values()):
        e.position = old_e.position
        e.incoming_connections = old_e.incoming_connections
    element_to_relocate = random.choice(list(new_elements.values()))
    element_to_relocate.position = (
        random.randint(0, max_x - element_to_relocate.width),
        random.randint(0, max_y - element_to_relocate.height)
    )
    return new_elements

def optimize_placement(elements, elements_dict, connection_points_dict, connection_delay, max_x, max_y, start_temp, cooling_factor, max_iterations):
    curr_layout = elements_dict
    current_delay = compute_critical_delay(elements, elements_dict, connection_points_dict, connection_delay)
    best_layout = curr_layout
    max_delay = current_delay
    temp = start_temp
    i = max_iterations
    j = 0
    while i > 0:
        candidate_layout = genarate_neighbour_all(curr_layout, max_x, max_y)
        if check_for_overlap(candidate_layout):
            continue
        candidate_energy = compute_critical_delay(candidate_layout.values(), candidate_layout, connection_points_dict, connection_delay)
        cost_difference = candidate_energy - current_delay

        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temp):
            curr_layout = candidate_layout
            current_delay = candidate_energy

            if current_delay < max_delay:
                best_layout = curr_layout
                max_delay = current_delay
        j = i
        temp *= cooling_factor
        # print(f'Iteration {i}: Temperature = {temp:.2f}, Current cost = {current_delay}')
        i-= 1

    return best_layout, max_delay

def find_non_overlapping_position(elements, width, height, max_x, max_y):
    attempts = 0
    max_attempts = 1000
    while attempts < max_attempts:
        x = random.randint(0, max_x - width)
        y = random.randint(0, max_y - height)
        if all(not (x < e.position[0] + e.width and x + width > e.position[0] and
                    y < e.position[1] + e.height and y + height > e.position[1]) for e in elements):
            return x, y
        attempts += 1
    raise ValueError("Unable to find a non-overlapping position after maximum attempts")

def parse_input(filename: str):
    elements = []
    connections = []
    elements_dict = {}
    connection_points_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue

            if parts[0] == 'pins':
                element_name = parts[1]
                connection_points = {f'{element_name}.p{i // 2}': ConnectionPoint(element_name, f'p{i//2}', (int(parts[i]), int(parts[i + 1]))) for i in range(2, len(parts), 2)}
                elements_dict[element_name].connection_points = connection_points
                for point_id, point in connection_points.items():
                    connection_points_dict[point_id] = point

            elif parts[0] == 'wire':
                e1, p1 = parts[1].split('.')
                e2, p2 = parts[2].split('.')
                connection = Connection(e1, p1, e2, p2)
                connection_points_dict[f'{e1}.{p1}'].connect(connection)
                connection_points_dict[f'{e2}.{p2}'].connect(connection)
                elements_dict[e1].connect(connection)
                elements_dict[e2].connect(connection)
                connections.append(connection)
            elif parts[0] == 'wire_delay':
                connection_delay = int(parts[1])
            else:
                name, width, height, latency = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
                element = CircuitElement(name, width, height, {}, latency)
                elements.append(element)
                elements_dict[name] = element

    return elements, connections, connection_points_dict, elements_dict, connection_delay

def save_output(filename, elements, elements_dict, connection_points_dict, connection_delay):
    connection_points_dict, elements_dict = update_final_postsn(connection_points_dict, elements_dict)
    min_x = min(element.position[0] for element in elements)
    min_y = min(element.position[1] for element in elements)
    for element in elements:
        element.position = (element.position[0] - min_x, element.position[1] - min_y)
    layout_dimensions = (
        max(element.position[0] + element.width for element in elements),
        max(element.position[1] + element.height for element in elements)
    )
    critical_delay = compute_critical_delay(elements, elements_dict, connection_points_dict, connection_delay)
    critical_path = identify_critical_path(elements, elements_dict, connection_points_dict, connection_delay)
    with open(filename, 'w') as file:
        file.write(f"bounding_box {layout_dimensions[0]} {layout_dimensions[1]}\n")
        file.write(f"critical_path {' '.join(path_element for path_element in critical_path)}\n")
        file.write(f"critical_path_delay {critical_delay}\n")
        for gate in elements_dict.values():  # Accessing values directly
            x, y = gate.position
            file.write(f"{gate.identifier} {x} {y}\n")

def calculate_max(elements):
    high_y = 0
    i = len(elements)-1
    while i >= 0:
        if high_y < elements[i].width:
            high_y = elements[i].width
        i -= 1
    return high_y

def main(input_file='input.txt', output_file='output.txt'):
    elements, connections, connection_points_dict, elements_dict, connection_delay = parse_input(input_file)
    
    max_x = sum(element.width for element in elements) + len(elements)
    max_y = calculate_max(elements) * 2
    
    for element in elements:
        element.position = find_non_overlapping_position(elements, element.width, element.height, max_x, max_y)
    
    for element in elements:
        elements_dict[element.identifier].position = element.position
    
    best_layout, path_delay = optimize_placement(elements, elements_dict, connection_points_dict, connection_delay, max_x, max_y, 1000, 0.99, 10000)
    
    save_output(output_file, elements,best_layout, connection_points_dict, connection_delay)

if __name__ == "__main__":
    main()