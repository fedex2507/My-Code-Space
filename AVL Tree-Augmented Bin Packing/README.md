# Cargo Management System Utilizing AVL Trees for Bin Packing Efficiently  

This project implements a **Cargo Management System (GCMS)** that leverages a modified **bin packing algorithm** and **AVL trees** to efficiently manage resources under capacity constraints. The system ensures optimal space utilization and O(log n) efficiency for operations like insertion, search, and deletion.  

---

## Features  
- **Modified Bin Packing Algorithm**:  
  Optimally allocates objects to bins under capacity constraints using AVL trees for dynamic management.  

- **Generalized Capacity Management System (GCMS)**:  
  - Manages bins and objects based on capacity and ID.  
  - Adapts to varying object sizes and bin capacities.  

- **AVL Tree Integration**:  
  - Employs balanced AVL trees for efficient operations.  
  - Ensures O(log n) efficiency for insertion, search, and deletion.  

- **Exception Handling**:  
  - Provides robust mechanisms to handle capacity violations gracefully.  
  - Ensures stability in memory-limited environments.  

---

## How It Works  
1. **Input Representation**:  
   - Bins and objects are initialized with their respective properties (capacity, ID, size, etc.).  

2. **Modular Design**:  
   - The system is divided into modules for AVL tree logic, object and bin representation, exception handling, and the GCMS core logic.  

3. **AVL Tree-Based Operations**:  
   - Manages objects and bins with AVL tree operations for dynamic and balanced resource allocation.  

4. **Bin Packing Algorithm**:  
   - Allocates objects to the most suitable bin dynamically while adhering to capacity constraints.  

5. **Exception Handling**:  
   - Detects and handles cases where objects exceed bin capacities or bins run out of space.  

6. **Output**:  
   - Provides a detailed report of bin utilization and object placement.  
   - Highlights exceptions (if any) encountered during allocation.  

---

## File Structure  
- `avl.py`: Implements the AVL tree structure and its operations (insertion, deletion, search).  
- `object.py`: Defines the `Object` class, encapsulating object properties (ID, size, etc.).  
- `node.py`: Defines the `Node` class for AVL tree nodes.  
- `gcms.py`: Core implementation of the Generalized Capacity Management System.  
- `exceptions.py`: Contains custom exceptions to handle capacity violations and other errors.  
- `bin.py`: Defines the `Bin` class, encapsulating bin properties (ID, capacity, current usage).  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/ShogunYash/My-Code-Space/AVL Tree-Augmented Bin Packing.git  

