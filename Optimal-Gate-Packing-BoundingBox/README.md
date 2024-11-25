# Efficient Gates Packing for Optimal Bounding Box Calculation  

This project presents an advanced **block-packing algorithm** designed to calculate the optimal bounding box for gate layouts. By leveraging a **binary tree structure**, the algorithm dynamically manages space, ensuring efficient utilization and balanced growth across packing scenarios.  

---

## Features  
- **Binary Tree-Based Packing**:  
  Utilizes a binary tree structure for managing space dynamically, enabling efficient packing strategies.  

- **Flexible Strategies**:  
  Supports both fixed-size and growth-based strategies, adjusting packing configurations based on block orientations to minimize bounding box dimensions.  

- **Node Splitting and Space Handling**:  
  - Recursively searches for suitable nodes to place blocks.  
  - Dynamically splits nodes to handle occupied space and optimize layout structure.  

- **Heuristic-Driven Growth**:  
  Incorporates heuristics to balance horizontal and vertical growth, ensuring optimal space utilization and minimal bounding box size.  

---

## How It Works  
1. **Input Representation**:  
   - Blocks are provided with dimensions and orientations.  
   - The algorithm processes these inputs to identify optimal packing strategies.  

2. **Binary Tree Structure**:  
   - A binary tree is initialized to manage space dynamically.  
   - Each node represents a region of the bounding box and is split as blocks are placed.  

3. **Recursive Node Search and Splitting**:  
   - The algorithm recursively searches for fitting nodes.  
   - Nodes are split to handle used space while maintaining an efficient tree structure.  

4. **Heuristic Guidance**:  
   - Heuristics guide growth in horizontal and vertical directions.  
   - Balances tree expansion to minimize bounding box area.  

5. **Output**:  
   - Outputs the dimensions of the minimal bounding box and the block placements.  

---

## Project Structure  
- `Gate-Packing.py`: Single file containing the complete implementation of the block-packing algorithm.  
- `README.md`: Comprehensive guide to the project.   
- `Theory.pdf`: Detailed documentation on the algorithm's design and performance analysis.  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/Wiring-Aware-Gate-Placement.git   

