# CPU Scheduling Algorithms Simulator

## About The Project
This project implements three fundamental CPU scheduling algorithms in Python:
- First-Come, First-Served (FCFS)
- Shortest Job First (SJF) - Non-preemptive version
- Round Robin (RR)

The simulator calculates key performance metrics for each algorithm including turnaround time, waiting time, and response time.

## Implemented Algorithms

### FCFS (First-Come, First-Served)
- Processes are executed in order of arrival
- Simple implementation with O(n) complexity
- May result in convoy effect

### SJF (Shortest Job First)
- Non-preemptive version
- Selects process with shortest burst time
- Minimizes average waiting time
- Requires knowledge of next CPU burst length

### Round Robin
- Uses time quantum for fair allocation
- Preemptive scheduling
- Good for time-sharing systems
- Performance depends on quantum size



# Ouput Example:
```python
FCFS Results:
Average Turnaround Time: 12.25
Average Waiting Time: 6.75
Average Response Time: 6.75

SJF (Non-preemptive) Results:
Average Turnaround Time: 10.75
Average Waiting Time: 5.25
Average Response Time: 5.25

Round Robin (Time Quantum=4) Results:
Average Turnaround Time: 13.50
Average Waiting Time: 8.00
Average Response Time: 2.50
```