import heapq

def sjf_priority_queue(processes, arrival_time, burst_time):
    n = len(processes)

    # Create a list to store the remaining burst time for each process
    remaining_time = burst_time.copy()

    # Initialize variables to track waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    current_time = 0  # Initialize current time to 0
    completed = 0     # Number of processes completed

    # Priority queue to store (burst_time, process) pairs
    priority_queue = []

    while completed < n:
        # Add processes that have arrived to the priority queue
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                heapq.heappush(priority_queue, (remaining_time[i], i))

        if not priority_queue:
            # If no process has arrived, increment the current time
            current_time += 1
        else:
            # Execute the process with the shortest remaining burst time
            burst, process = heapq.heappop(priority_queue)
            remaining_time[process] -= 1
            current_time += 1

            if remaining_time[process] == 0:
                # Process has completed
                completed += 1
                # Calculate waiting time and turnaround time for the completed process
                waiting_time[process] = current_time - arrival_time[process] - burst_time[process]
                turnaround_time[process] = current_time - arrival_time[process]

    # Calculate and print the average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Print the table
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

    return processes

'''if __name__ == "__main__":
    # Example usage:
    processes = [1, 2, 3, 4]
    arrival_time = [0, 1, 2, 3]
    burst_time = [6, 8, 7, 4]
    sjf_priority_queue(processes, arrival_time, burst_time)'''
