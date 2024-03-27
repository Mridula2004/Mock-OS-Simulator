def fcfs(processes, arrival_time, burst_time):
    n = len(processes)

    # Initialize the waiting time for the first process as 0
    waiting_time = [0] * n

    # Calculate waiting time for all other processes
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate turnaround time for each process
    turnaround_time = [0] * n
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calculate and print the average waiting time and turnaround time
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

    return processes
