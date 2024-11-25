# Dynamic Load Balancing and Priority Scheduling for Distributed Task Management  

This project implements a **dynamic load balancing system** and **priority-based scheduling** framework for distributed environments. The system is designed to optimize resource usage, minimize task delays, and ensure reliable task execution with real-time monitoring and fault tolerance.  

---

## Features  
- **Dynamic Load Balancing**:  
  - Redistributes tasks dynamically to prevent workload imbalances.  
  - Optimizes resource utilization across distributed nodes.  

- **Priority-Based Scheduling**:  
  - Ensures timely execution of high-priority tasks.  
  - Implements a custom heap structure to manage task priorities efficiently.  

- **Real-Time Monitoring and Reallocation**:  
  - Continuously monitors tasks and nodes to detect workload changes.  
  - Reallocates tasks dynamically to maintain system efficiency.  

- **Fault-Tolerant Framework**:  
  - Ensures reliable task execution despite node failures.  
  - Implements redundancy and recovery mechanisms.  

---

## How It Works  
1. **Input Representation**:  
   - Tasks are defined with attributes such as priority, size, and execution time.  
   - Nodes are represented with their current workloads and capacities.  

2. **Dynamic Load Balancing**:  
   - Tasks are allocated to nodes based on current workloads.  
   - Reallocation occurs when workload imbalances are detected.  

3. **Priority Scheduling**:  
   - Uses a custom heap-based priority queue to manage tasks.  
   - High-priority tasks are scheduled for execution before lower-priority tasks.  

4. **Fault Tolerance**:  
   - Redundancy mechanisms ensure task execution even if a node fails.  
   - Recovery protocols dynamically reassign tasks to operational nodes.  

5. **Output**:  
   - Displays task allocation, execution schedules, and node workloads.  
   - Provides logs for fault recovery and task reallocations.  

---

## File Structure  
- `crewmate.py`: Implements the task and node monitoring framework, handling real-time updates and reallocation.  
- `heap.py`: Contains the custom heap implementation for priority-based scheduling.  
- `straw-hat.py`: Core logic for load balancing and task allocation across distributed nodes.  
- `treasure.py`: Manages task attributes, including priority, size, and execution time, and provides utilities for task creation and monitoring.  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/ShogunYash/My-Code-Space/Distributed-Load-Scheduler.git  

