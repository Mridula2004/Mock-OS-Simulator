def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)

    # Initialize variables to track waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_time = burst_time.copy()
    current_time = 0
    completed = 0
    queue = []

    while completed < n:
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                queue.append(i)

        if not queue:
            current_time += 1
        else:
            process = queue.pop(0)
            if remaining_time[process] > time_quantum:
                current_time += time_quantum
                remaining_time[process] -= time_quantum
                queue.append(process)
            else:
                current_time += remaining_time[process]
                waiting_time[process] = current_time - arrival_time[process] - burst_time[process]
                turnaround_time[process] = current_time - arrival_time[process]
                completed += 1
                remaining_time[process] = 0

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

    return processes

'''if __name__ == "__main__":
    # Example usage:
    processes = [1, 2, 3, 4]
    arrival_time = [0, 1, 2, 3]
    burst_time = [8, 6, 10, 7]
    time_quantum = 2
    round_robin(processes, arrival_time, burst_time, time_quantum)'''
