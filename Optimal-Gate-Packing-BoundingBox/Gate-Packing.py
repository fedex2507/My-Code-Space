import tkinter as tk
import random

class Block:
    def __init__(self, name, w, h, num=1):
        self.name = name
        self.w = w
        self.h = h
        self.num = num
        self.area = w * h
        self.fit = None

class Packer:
    def __init__(self, w=None, h=None):
        if w and h:
            self.init(w, h)
        else:
            self.root = None

    def init(self, w, h):
        """Initialize root for fixed-size packing."""
        self.root = {'x': 0, 'y': 0, 'w': w, 'h': h}

    def fit(self, blocks):
        """Fit blocks either in fixed-size or growing mode based on initialization."""
        if self.root:  # Fixed-size packing
            for block in blocks:
                node = self.find_node(self.root, block.w, block.h)
                if node:
                    block.fit = self.split_node(node, block.w, block.h)
        else:  # Growing packing
            if not blocks:
                return

            # Initialize root with the dimensions of the first block
            self.root = {'x': 0, 'y': 0, 'w': blocks[0].w, 'h': blocks[0].h}

            for block in blocks:
                node = self.find_node(self.root, block.w, block.h)
                if node:
                    block.fit = self.split_node(node, block.w, block.h)
                else:
                    block.fit = self.grow_node(block.w, block.h)

    def find_node(self, root, w, h):
        """Recursively find a suitable node where the block can fit."""
        if root.get('used'):
            return self.find_node(root.get('right', {}), w, h) or self.find_node(root.get('down', {}), w, h)
        elif w <= root['w'] and h <= root['h']:
            return root
        else:
            return None

    def split_node(self, node, w, h):
        """Split the node after placing the block."""
        node['used'] = True
        node['down'] = {'x': node['x'], 'y': node['y'] + h, 'w': node['w'], 'h': node['h'] - h}
        node['right'] = {'x': node['x'] + w, 'y': node['y'], 'w': node['w'] - w, 'h': h}
        return node

    def grow_node(self, w, h):
        """Determine the best way to grow the root to fit the new block."""
        can_grow_down = (w <= self.root['w'])
        can_grow_right = (h <= self.root['h'])

        should_grow_right = can_grow_right and (self.root['h'] >= (self.root['w'] + w))
        should_grow_down = can_grow_down and (self.root['w'] >= (self.root['h'] + h))

        if should_grow_right:
            return self.grow_right(w, h)
        elif should_grow_down:
            return self.grow_down(w, h)
        elif can_grow_right:
            return self.grow_right(w, h)
        elif can_grow_down:
            return self.grow_down(w, h)
        else:
            return None  # If neither growth option is possible

    def grow_right(self, w, h):
        """Grow the root to the right to accommodate the new block."""
        self.root = {
            'used': True,
            'x': 0,
            'y': 0,
            'w': self.root['w'] + w,
            'h': self.root['h'],
            'down': self.root,
            'right': {'x': self.root['w'], 'y': 0, 'w': w, 'h': self.root['h']}
        }
        node = self.find_node(self.root, w, h)
        if node:
            return self.split_node(node, w, h)
        else:
            return None

    def grow_down(self, w, h):
        """Grow the root downwards to accommodate the new block."""
        self.root = {
            'used': True,
            'x': 0,
            'y': 0,
            'w': self.root['w'],
            'h': self.root['h'] + h,
            'down': {'x': 0, 'y': self.root['h'], 'w': self.root['w'], 'h': h},
            'right': self.root
        }
        node = self.find_node(self.root, w, h)
        if node:
            return self.split_node(node, w, h)
        else:
            return None

class DemoApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=1000, height=1000)
        self.canvas.pack()
        self.blocks = []
        self.scale = 25  # Default scale factor

        self.init_ui()

    def init_ui(self):
        self.run()

    def run(self):
        blocks1, blocks2 = self.take_input()

        packer1 = Packer()
        packer2 = Packer()

        packer1.fit(blocks1)
        packer2.fit(blocks2)

        area1 = packer1.root['w'] * packer1.root['h']
        area2 = packer2.root['w'] * packer2.root['h']

        if area1 <= area2:
            print(f"bounding_box {packer1.root['w']} {packer1.root['h']}")
            self.write_output("input.txt", "output.txt", blocks1, packer1)
            self.draw_blocks(blocks1, packer1.root['w'], packer1.root['h'])
        else:
            print(f"bounding_box {packer2.root['w']} {packer2.root['h']}")
            self.write_output("input.txt", "output.txt", blocks2, packer2)
            self.draw_blocks(blocks2, packer2.root['w'], packer2.root['h'])

    def write_output(self, dim_file_name, coord_file_name, blocks, packer):
        with open(dim_file_name, "w") as dim_file, open(coord_file_name, "w") as coord_file:
            coord_file.write(f"bounding_box {packer.root['w']} {packer.root['h']}\n")
            for block in blocks:
                if block.fit:
                    dim_file.write(f"{block.name} {block.w} {block.h}\n")
                    coord_file.write(f"{block.name} {block.fit['x']} {block.fit['y']}\n")
                    print(f"{block.name} {block.fit['x']} {block.fit['y']}")

    def take_input(self):
        blocks1 = []
        blocks2 = []
        t = int(input("Enter the number of gates: "))
        self.scale = int(input("Enter the scaling factor: "))
        for i in range(t):
            name, h, w = input().split()
            h = int(h)
            w = int(w)
            blocks1.append(Block(name, min(w, h), max(w, h)))
            blocks2.append(Block(name, max(w, h), min(w, h)))

        sorted_blocks1 = sorted(blocks1, key=lambda block: max(block.w, block.h), reverse=True)
        sorted_blocks2 = sorted(blocks2, key=lambda block: max(block.w, block.h), reverse=True)

        return sorted_blocks1, sorted_blocks2

    def draw_blocks(self, blocks, width, height):
        scale = self.scale
        self.canvas.delete("all")
        self.canvas.config(width=scale * width, height=scale * height)

        for block in blocks:
            if block.fit:
                x = block.fit['x'] * scale
                y = block.fit['y'] * scale
                w = block.w * scale
                h = block.h * scale
                color = self.random_color()
                self.canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline="black")
                self.canvas.create_text(x + w / 2, y + h / 2, text=block.name, fill="white", font=("Arial", 12, "bold"))

        # Draw grid on top of everything to cover the entire bounding box
        self.draw_grid(scale * width, scale * height, scale)

    def draw_grid(self, width, height, scale):
        for i in range(0, width, scale):
            self.canvas.create_line(i, 0, i, height, fill="gray")
        for j in range(0, height, scale):
            self.canvas.create_line(0, j, width, j, fill="gray")

    def random_color(self):
        return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

if __name__ == "__main__":
    root = tk.Tk()
    app = DemoApp(root)
    root.mainloop()
