import tkinter as tk
from tkinter import ttk
import DeadLock as dl
import bt as create_bt
import FCFS as fcfs
import SJF as sjf
import RoundRobin as rr

def main2(n):
    def validate_and_next():
        selected_processes = [process_vars[i].get() for i in range(n)]

        # Check if all dropdowns are filled
        if all(process for process in selected_processes):
            next_window(selected_processes)
        else:
            validation_label.config(text="Please select processes for all dropdowns.")

    def next_window(processes):
        at = []
        chosen_processes = []
        # Close the current window
        root.destroy()

        # Create a new window for the next step
        next_window = tk.Tk()
        next_window.title("Check for Deadlock")

        # Display selected processes in the new window
        for i, process in enumerate(processes, 1):
            chosen_processes.append(process)
        for i in range(n):
            at.append(i)
        BT = create_bt.burstTime(chosen_processes)
        dl.is_deadlock(chosen_processes)

        def firstComeFirstServe():
            ordered_processes = fcfs.fcfs(chosen_processes, at, BT)

        def shortestJobFirst():
            ordered_processes = sjf.sjf_priority_queue(chosen_processes, at, BT)

        def roundRobin():
            def on_okay():
                time_quantum = int(entry.get())
                ordered_processes = rr.round_robin(chosen_processes, at, BT, time_quantum)
                # You can do something with the ordered_processes if needed

            # Create a textbox for entering the time quantum
            entry_label = tk.Label(next_window, text="Enter the time quantum:")
            entry_label.pack()

            entry = tk.Entry(next_window)
            entry.pack()

            button_okay = tk.Button(next_window, text="Okay", command=on_okay)
            button_okay.pack()

        if dl.is_deadlock(chosen_processes):
            label = tk.Label(next_window, text=f"Deadlock")
            label.pack()
        else:
            label = tk.Label(next_window, text=f"No Deadlock")
            label.pack()
            # Create three buttons
            button1 = tk.Button(next_window, text="FCFS", command=firstComeFirstServe)
            button1.pack()
            button2 = tk.Button(next_window, text="SJF", command=shortestJobFirst)
            button2.pack()

            button3 = tk.Button(next_window, text="Round Robin", command=roundRobin)
            button3.pack()

        next_window.mainloop()

    # Create the main window
    root = tk.Tk()
    root.title("Process Selection")

    process_vars = [tk.StringVar() for _ in range(n)]

    # Create dropdown boxes for each process
    for i in range(n):
        label = tk.Label(root, text=f"Process {i + 1}:")
        label.pack()

        process_dropdown = ttk.Combobox(root, textvariable=process_vars[i], values=["Create Folder", "Read File", "Delete File", "Write File", "Plug Device"])
        process_dropdown.pack()

    # Create a button to validate and proceed to the next window
    next_button = tk.Button(root, text="Next", command=validate_and_next)
    next_button.pack()

    validation_label = tk.Label(root, text="")
    validation_label.pack()

    root.mainloop()
