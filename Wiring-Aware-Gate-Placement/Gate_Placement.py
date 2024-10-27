from typing import List, Optional, Set, Dict

class Gate:
    def __init__(self, name: str, horizontal: int, vertical: int, pins: List[tuple]):
        self.name = name
        self.horizontal = horizontal
        self.vertical = vertical
        self.pins = pins
        self.position = [0, 0] # Default bottom-left position of the gate

class Wire:
    def __init__(self, pin1: str, pin2: str):
        self.pin1 = pin1  # (gate_name, pin_number)
        self.pin2 = pin2  # (gate_name, pin_number)

class Grid:
    def __init__(self, horizontal: int, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical
        self.occupied = set()

    def is_empty(self, x: int, y: int, w: int, h: int) -> bool:
        """Check if the space is available for a gate."""
        if x + w > self.horizontal or y + h > self.vertical:
            return False
        return all((i, j) not in self.occupied for i in range(x, x + w) for j in range(y, y + h))

    def gate_occupied(self, location: list[int, int], w: int, h: int):
        """Mark the grid cells occupied by a gate."""
        x, y = location
        for i in range(x, x + w):
            for j in range(y, y + h):
                self.occupied.add((i, j))

    def pack_gate(self, gate: Gate, position: List[int]) -> List[int]:
        """Place the gate at a specified position."""
        x, y = position
        if self.is_empty(x, y, gate.horizontal, gate.vertical):
            gate.position = [x,y]  # Set the gate's position as a list
            self.gate_occupied((x, y), gate.horizontal, gate.vertical)
            return position
        else:
            return None

    def grow_box(self, factor: float = 1.5):
        """Increase the grid size by a factor to accommodate more gates."""
        self.horizontal = int(self.horizontal * factor)
        self.vertical = int(self.vertical * factor)

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x: str) -> str:
        """Find the representative of the set that contains x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: str, y: str):
        """Merge the sets that contain x and y."""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] - self.rank[rootY] > 0:
                self.parent[rootY] = rootX
            elif self.rank[rootX] - self.rank[rootY] < 0:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add(self, x: str):
        """Add a new element with itself as the parent."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def retrive_clusters(self) -> List[Set[str]]:
        """Return the clusters of connected pins."""
        clusters = {}
        for pin in self.parent:
            root = self.find(pin)
            if root not in clusters:
                clusters[root] = set()
            clusters[root].add(pin)
        return list(clusters.values())

def make_clusters(gates: Dict[str, Gate], wires: List[Wire]) -> List[Set[str]]:
    uf = UnionFind()

    # Add all pins to the union-find structure
    for gate in gates.values():
        for i, pin in enumerate(gate.pins):
            pin_identifier = f"{gate.name}.p{i + 1}"
            uf.add(pin_identifier)

    # Union the pins that are connected by wires
    for wire in wires:
        gate1_name, pin1 = wire.pin1.split('.')
        gate2_name, pin2 = wire.pin2.split('.')
        if gate1_name != gate2_name:  # Ensure pins belong to different gates
            uf.union(wire.pin1, wire.pin2)

    return uf.retrive_clusters()
def get_min(positions: List[List[int]], i) -> List[int]:
    """Get the minimum x and y coordinates from a list of positions."""
    minimum = positions[0][i]
    for pos in positions:
        if minimum > pos[i]:
            minimum = pos[i]
    return minimum

def calculate_pre_bounding_box(positions: List[List[int]], gates: Dict[str, Gate]) -> tuple:
    """Calculate the bounding box of a set of gate positions."""
    min_x = get_min(positions, 0)
    max_x = max(pos[0] for pos in positions)
    min_y = get_min(positions, 1)
    max_y = max(pos[1] for pos in positions)
    return max_x - min_x, max_y - min_y

def calculate_final_bounding_box(positions: List[List[int]], gates: Dict[str, Gate]) -> tuple:
    """Calculate the final bounding box of a set of gate positions."""
    min_x = get_min(positions, 0)
    max_x = max(gate.position[0] + gate.horizontal for gate in gates.values())
    min_y = get_min(positions, 1)
    max_y = max(gate.position[1] + gate.vertical for gate in gates.values())

    # Update positions to be lists (they should be mutable)
    for gate in gates.values():
        gate.position[0] -= min_x
        gate.position[1] -= min_y

    return max_x - min_x, max_y - min_y

def manhattan_distance(positions: List[List[int]], gates: Dict[str, Gate]) -> int:
    """Calculate the semi-perimeter of the bounding box for a set of gate positions."""
    horizontal, vertical = calculate_pre_bounding_box(positions, gates)
    return horizontal + vertical

def generate_perimeter_positions(gate_name: str, gate_position: List[int], gates: Dict[str, Gate], perimeter_positions: Set[tuple]) -> Set[tuple]:
    x, y = gate_position
    gate = gates[gate_name]

    for i in range(gate.horizontal):
        perimeter_positions.add((x + i, y, "bottom"))  # Below (top side)
        perimeter_positions.add((x + i, y + gate.vertical, "top"))  # Above (bottom side)

    for j in range(gate.vertical):
        perimeter_positions.add((x, y + j, "left"))  # Left side
        perimeter_positions.add((x + gate.horizontal, y + j, "right"))  # Right side

    return perimeter_positions
def update_gate_placement(gate: Gate, best_gate_position: tuple, preffered_position: tuple, grid: Grid, gates: Dict[str, Gate], candidate_positions: Set[tuple], packed_gates: Set[str], packed_gates_position: Set[tuple], cluster_positions: List[tuple]) -> Set[tuple]:
    """Update gate placement and candidate positions."""
    grid.pack_gate(gate, best_gate_position)
    packed_gates_position.add((gate.name, best_gate_position))
    packed_gates.add(gate.name)
    cluster_positions.append(preffered_position)
    candidate_positions = generate_perimeter_positions(gate.name, best_gate_position, gates, candidate_positions)
    return candidate_positions

def _place_gate(gate: Gate, grid: Grid, candidate_positions: Set[tuple], packed_gates: Set[str], packed_gates_position: Set[tuple], gates: Dict[str, Gate], pin_number: str, cluster_positions: List[tuple]) -> tuple:
    """Logic to place a gate at the optimal position."""
    preffered_position = None
    best_semi_perimeter = float('inf')
    best_gate_position = None

    for x, y, z in candidate_positions:
        if z == "bottom":
            y -= gate.vertical
        if z == "left":
            x -= gate.horizontal
        if grid.is_empty(x, y, gate.horizontal, gate.vertical):
            relative_pin_coordinates = gate.pins[int(pin_number[1]) - 1]
            temp_position = (x + relative_pin_coordinates[0], y + relative_pin_coordinates[1])
            cluster_positions.append(temp_position)
            semi_perimeter = manhattan_distance(cluster_positions, gates)

            if semi_perimeter < best_semi_perimeter:
                best_semi_perimeter = semi_perimeter
                preffered_position = temp_position
                best_gate_position = (x, y)

            cluster_positions.pop()
        else:
            if z == "bottom":
                y += gate.vertical
            elif z == "left":
                x += gate.horizontal

    if preffered_position:
       candidate_positions = update_gate_placement(gate, best_gate_position, preffered_position, grid, gates, candidate_positions, 
                            packed_gates, packed_gates_position, cluster_positions)

    return candidate_positions

def pack_gates(grid: Grid, gates: Dict[str, Gate], clusters: List[Set[str]]) -> tuple:
    packed_gates = set()
    packed_gates_position = set()
    total_wire_length = 0

    # Sort clusters by the number of pins (largest to smallest)
    sorted_clusters = sorted(clusters, key=len, reverse=True)
    candidate_positions = set()

    for cluster in sorted_clusters:
        cluster_positions = []

        for pin in cluster:
            gate_name, pin_number = pin.split('.')
            gate = gates[gate_name]
            if gate_name in packed_gates:
                relative_pin_coordinates = gate.pins[int(pin_number[1]) - 1]
                cluster_positions.append((gate.position[0] + relative_pin_coordinates[0], gate.position[1] + relative_pin_coordinates[1]))

        for pin in cluster:
            gate_name, pin_number = pin.split('.')
            gate = gates[gate_name]

            if gate_name not in packed_gates:
                if not packed_gates_position:
                    grid.pack_gate(gate, [0, 0])
                    packed_gates_position.add((gate_name, (0, 0)))
                    packed_gates.add(gate_name)
                    relative_pin_coordinates = gate.pins[int(pin_number[1]) - 1]
                    temp_position = [relative_pin_coordinates[0], relative_pin_coordinates[1]]
                    cluster_positions.append(temp_position)
                    candidate_positions = generate_perimeter_positions(gate_name, [0, 0], gates, candidate_positions)
                    continue

                # Call the new function to place the gate
                candidate_positions = _place_gate(gate, grid, candidate_positions, packed_gates, packed_gates_position, gates, pin_number, cluster_positions)

        if cluster_positions:
            total_wire_length += manhattan_distance(cluster_positions, gates)

    return packed_gates_position, total_wire_length


def save_output(file_path: str, gates: Dict[str, Gate], total_wire_length: int):
    """Save the gate positions and total wire length to a file."""
    placed_positions = [gate.position for gate in gates.values()]
    horizontal, vertical = calculate_final_bounding_box(placed_positions, gates)

    with open(file_path, 'w') as file:
        file.write(f"bounding_box {horizontal} {vertical}\n")
        for gate in gates.values():
            file.write(f"{gate.name} {gate.position[0]} {gate.position[1]}\n")
        file.write(f"total wire length {total_wire_length}\n")

def Take_input(file_path: str) -> tuple:
    """Parse the input file to extract gates and wires information."""
    try:
        gates = {}
        wires = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            current_gate = None
            for line in lines:
                parts = line.split()
                if len(parts) == 0:
                    continue  # Skip empty lines
                if parts[0][0] == 'g':  # Gate definition, e.g. "g1 3 3"
                    gate_name = parts[0]
                    horizontal = int(parts[1])
                    vertical = int(parts[2])
                    gates[gate_name] = Gate(gate_name, horizontal, vertical, [])
                    current_gate = gates[gate_name]
                elif parts[0] == 'pins' and current_gate:  # Pin coordinates, e.g. "pins g1 0 1 0 2"
                    for i in range(2, len(parts), 2):
                        pin_x = int(parts[i])
                        pin_y = int(parts[i + 1])
                        current_gate.pins.append((pin_x, pin_y))
                elif parts[0] == 'wire':  # Wire definition, e.g. "wire g3.p2 g7.p1"
                    wire1 = parts[1].split('.')
                    wire2 = parts[2].split('.')
                    gate1 = wire1[0]
                    pin1 = int(wire1[1][1:])  # Remove the 'p' from the pin number
                    gate2 = wire2[0]
                    pin2 = int(wire2[1][1:])  # Remove the 'p' from the pin number
                    wire = Wire(f"{gate1}.p{pin1}", f"{gate2}.p{pin2}")
                    wires.append(wire)

        return gates, wires

    except FileNotFoundError:
        print("File not found")
        return None, None
    except Exception as e:
        print("Error parsing input file: ", str(e))
        return None, None

# Main execution
if __name__ == "__main__":
    gates, wires = Take_input('input.txt')
    if gates and wires:
        grid = Grid(500000, 500000)
        clusters = make_clusters(gates, wires)
        packed_gates_position, total_wire_length = pack_gates(grid, gates, clusters)
        save_output('output.txt', gates, total_wire_length)

