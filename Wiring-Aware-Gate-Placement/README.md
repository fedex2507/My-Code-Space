# Wiring Aware Gate Positioning for Optimal Wire Length Calculation  

This project focuses on designing a **grid-based gate placement algorithm** to optimize wire length in integrated circuit layouts. The implementation employs advanced heuristics and clustering techniques for efficient gate positioning and wiring-aware placement.  

---

## Features  
- **Grid-Based Gate Placement**:  
  Designed an algorithm to position gates on a grid, minimizing wiring overhead.  

- **Union-Find Clustering**:  
  Employed the Union-Find data structure to cluster connected pins, facilitating efficient gate grouping.  

- **Manhattan Distance Heuristics**:  
  Used semi-perimeter-based placement decisions to minimize wire length through Manhattan distance calculations.  

- **Dynamic Space Optimization**:  
  - Implemented perimeter-based candidate generation.  
  - Included dynamic grid resizing to ensure optimal space utilization and wire routing.  

- **Iterative Clustering Strategies**:  
  Developed iterative strategies to balance wiring complexity and optimize gate layouts.  

---

## How It Works  
1. **Input Representation**:  
   The circuit is represented as a grid, with gates and pins specified as coordinates.  

2. **Clustering Using Union-Find**:  
   - Connected pins are grouped into clusters using the Union-Find data structure.  
   - Ensures gates within the same cluster are optimally positioned.  

3. **Wire Length Calculation**:  
   - Manhattan distance heuristics determine semi-perimeter wire lengths for placement decisions.  
   - Priority is given to configurations minimizing wiring complexity.  

4. **Dynamic Candidate Generation**:  
   - Perimeter-based candidate generation refines gate positions.  
   - Grid resizing adapts the layout for better utilization of available space.  

5. **Iterative Layout Optimization**:  
   - Gates are repositioned iteratively based on clustering and wire length feedback.  
   - Balances wiring complexity with layout compactness.  

---

## Project Structure  
- `Gate_Placement.py`: Main implementation of the grid-based gate placement algorithm.  
- `README.md`: Comprehensive guide to the project.  
- `Gate-Placement.pdf`: Documentation and analysis of placement strategies.  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/Wiring-Aware-Gate-Placement.git  

