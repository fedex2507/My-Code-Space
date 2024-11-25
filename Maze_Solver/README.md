# PacMan Maze Solver - DFS-Based Pathfinding Algorithm  

Welcome to the **PacMan Maze Solver**, a project designed to find the optimal path in a PacMan maze using a **Depth-First Search (DFS)** algorithm. This repository contains the implementation of a custom DFS-based pathfinding algorithm, utilizing data structures and advanced programming techniques to efficiently solve complex mazes.  

---

## Features  
- **DFS-Based Pathfinding**:  
  Utilizes a stack data structure to explore all possible routes in the maze while ensuring efficient backtracking.  

- **State-Space Search**:  
  Incorporates a state-space search approach to systematically explore maze paths, handling obstacles and boundaries effectively.  

- **Route Preservation**:  
  Implements a **copy-on-append strategy**, ensuring existing routes remain unmodified during exploration, which aids in backtracking and debugging.  

- **Custom Exception Handling**:  
  Introduces custom exceptions to gracefully manage cases where no valid path to the goal exists.  

---

## How It Works  
1. **Initialization**:  
   The maze is represented as a 2D grid, where walls, paths, the start point, and the goal are defined.  

2. **DFS Exploration**:  
   - A stack-based DFS algorithm is used to explore paths.  
   - The algorithm backtracks using the stack when dead ends are encountered.  

3. **Obstacle and Boundary Handling**:  
   The algorithm dynamically checks for obstacles (walls) and boundaries to prevent invalid moves.  

4. **Path Recording**:  
   - A copy-on-append strategy is employed to keep track of all potential paths.  
   - Ensures the algorithm can backtrack without altering previous routes.  

5. **Path Validation**:  
   If no valid path exists, a custom exception is raised to notify the user.  

---

## Project Structure  
- `maze_solver.py`: Main file containing the DFS-based algorithm implementation.  
- `exceptions.py`: Module defining custom exceptions for handling edge cases.  
- `README.md`: Comprehensive guide to the project.  
- `test_cases/`: Directory with sample maze grids for testing.  
- `docs/`: Documentation explaining the algorithm in depth.  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/PacMan-Maze-Solver.git  

