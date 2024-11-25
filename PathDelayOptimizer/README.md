# Minimization of Critical Path Delay using Simulated Annealing in Circuit Layout  

This project focuses on minimizing the critical path delay in circuit layouts through **Simulated Annealing**. It incorporates parsing intricate circuit specifications, optimizing gate placement, and evaluating delay factors to achieve efficient circuit designs.  

---

## Features  
- **Circuit Specification Parsing**:  
  Developed a robust parsing module to handle complex circuit inputs, including gate configurations, wiring details, and delay factors.  

- **Critical Path Identification**:  
  Algorithmically identified primary input and output nodes to ensure accurate propagation delay measurements.  

- **Simulated Annealing Optimization**:  
  - Employed simulated annealing to iteratively adjust gate positions for non-overlapping layouts.  
  - Aimed to minimize total delay along the critical path.  

- **Layout and Delay Optimization**:  
  - Systematically reduced circuit delay and layout area.  
  - Generated insights into critical paths and ensured performance constraints were met.  

---

## How It Works  
1. **Input Parsing**:  
   - Circuit specifications include gate configurations, wiring connections, and individual delays.  
   - The parsing module interprets these inputs into a usable format for analysis.  

2. **Critical Path Analysis**:  
   - Primary input and output nodes are identified.  
   - Propagation delays are calculated to determine the circuit's critical path.  

3. **Simulated Annealing for Optimization**:  
   - Iteratively adjusts gate positions to minimize critical path delay.  
   - Ensures non-overlapping gate placement and optimizes layout area.  

4. **Output Generation**:  
   - Final outputs highlight critical path delays and optimized gate layouts.  
   - Results meet performance constraints effectively.  

---

## Project Structure  
- `CircuitDelayMinimizer.py`: Contains algorithms for critical path identification and delay analysis. Implements the optimization logic for gate placement.     
- `README.md`: Comprehensive guide to the project.  
- `readme.pdf`: Documentation detailing the simulated annealing process and critical path insights.  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/ShogunYash/My-Code-Space/PathDelayOptimizer.git  

