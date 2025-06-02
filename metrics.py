class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = -1
        self.finish_time = -1
        self.waiting_time = 0
        self.response_time = -1
    
    def __str__(self):
        return f"Process {self.pid}: AT={self.arrival_time}, BT={self.burst_time}, ST={self.start_time}, FT={self.finish_time}"

def calculate_metrics(processes):
    total_tat = 0
    total_wt = 0
    total_rt = 0
    n = len(processes)
    
    for p in processes:
        tat = p.finish_time - p.arrival_time
        wt = tat - p.burst_time
        rt = p.response_time - p.arrival_time
        
        total_tat += tat
        total_wt += wt
        total_rt += rt
    
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n
    
    return avg_tat, avg_wt, avg_rt

def fcfs(processes):
    processes_sorted = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    
    for p in processes_sorted:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        
        p.start_time = current_time
        p.response_time = current_time
        current_time += p.burst_time
        p.finish_time = current_time
        p.remaining_time = 0
    
    return calculate_metrics(processes_sorted)

def sjf_non_preemptive(processes):
    processes_sorted = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    completed = []
    ready_queue = []
    
    while len(completed) < len(processes_sorted):
        # اضافه کردن فرآیندهای رسیده به صف آماده
        for p in processes_sorted:
            if p.arrival_time <= current_time and p not in completed and p not in ready_queue:
                ready_queue.append(p)
        
        if not ready_queue:
            current_time += 1
            continue
        
        # انتخاب فرآیند با زمان اجرای کوتاه‌تر
        ready_queue.sort(key=lambda x: x.burst_time)
        selected = ready_queue[0]
        
        selected.start_time = current_time
        selected.response_time = current_time
        current_time += selected.burst_time
        selected.finish_time = current_time
        selected.remaining_time = 0
        
        completed.append(selected)
        ready_queue.remove(selected)
    
    return calculate_metrics(processes_sorted)

def round_robin(processes, time_quantum):
    processes_sorted = sorted(processes, key=lambda x: x.arrival_time)
    current_time = 0
    ready_queue = []
    completed = []
    n = len(processes_sorted)
    
    # کپی کردن فرآیندها برای کار با remaining_time
    processes_copy = []
    for p in processes_sorted:
        new_p = Process(p.pid, p.arrival_time, p.burst_time)
        processes_copy.append(new_p)
    processes_sorted = processes_copy
    
    ready_queue.append(processes_sorted[0])
    current_time = processes_sorted[0].arrival_time
    next_process_idx = 1
    
    while len(completed) < n:
        if not ready_queue:
            if next_process_idx < n:
                next_process = processes_sorted[next_process_idx]
                current_time = next_process.arrival_time
                ready_queue.append(next_process)
                next_process_idx += 1
            else:
                current_time += 1
                continue
        
        current_process = ready_queue.pop(0)
        
        if current_process.start_time == -1:
            current_process.start_time = current_time
            current_process.response_time = current_time
        
        if current_process.remaining_time <= time_quantum:
            current_time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.finish_time = current_time
            completed.append(current_process)
            
            # اضافه کردن فرآیندهای جدیدی که رسیده‌اند
            while next_process_idx < n and processes_sorted[next_process_idx].arrival_time <= current_time:
                ready_queue.append(processes_sorted[next_process_idx])
                next_process_idx += 1
        else:
            current_time += time_quantum
            current_process.remaining_time -= time_quantum
            
            # اضافه کردن فرآیندهای جدیدی که رسیده‌اند
            while next_process_idx < n and processes_sorted[next_process_idx].arrival_time <= current_time:
                ready_queue.append(processes_sorted[next_process_idx])
                next_process_idx += 1
            
            ready_queue.append(current_process)
    
    return calculate_metrics(processes_sorted)

# تست الگوریتم‌ها با داده‌های نمونه
if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]
    
    print("FCFS Results:")
    avg_tat, avg_wt, avg_rt = fcfs([Process(p.pid, p.arrival_time, p.burst_time) for p in processes])
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")
    print()
    
    print("SJF (Non-preemptive) Results:")
    avg_tat, avg_wt, avg_rt = sjf_non_preemptive([Process(p.pid, p.arrival_time, p.burst_time) for p in processes])
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")
    print()
    
    print("Round Robin (Time Quantum=4) Results:")
    avg_tat, avg_wt, avg_rt = round_robin([Process(p.pid, p.arrival_time, p.burst_time) for p in processes], 4)
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")