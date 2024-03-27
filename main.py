import tkinter as tk
from tkinter import ttk

import os
import glob

import main2 as second_screen

# Define the path to the Desktop
desktop_path = os.path.expanduser("~/Desktop")

# Search for "marsh.png" on the Desktop
image_path = None
for file_path in glob.glob(os.path.join(desktop_path, "marsh.png")):
    image_path = file_path
    break

'''if image_path:
    print(f"Path to 'marsh.png' on the Desktop: {image_path}")
else:
    print("The 'marsh.png' image was not found on the Desktop.")'''


def next_window():
    # Get the number of processes entered in the textbox
    num_processes = entry.get()
    
    # Close the current window
    root.destroy()
    if num_processes:
        n=int(num_processes)
    # Create a new window for the next step
    second_screen.main2(n)
    
# Create the main window
root = tk.Tk()
root.title("Marshmellow OS")

# Load and display the image
photo = tk.PhotoImage(file=image_path)  # Replace YourUsername with your actual username
image_label = tk.Label(root, image=photo)
image_label.photo = photo
image_label.pack()

# Display the text
text_label = tk.Label(root, text="Welcome to Marshmellow OS")
text_label.pack()

# Create a textbox for entering the number of processes
entry_label = tk.Label(root, text="Enter the number of processes:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create a button to save the number and move to the next window
next_button = tk.Button(root, text="Next", command=next_window)
next_button.pack()



root.mainloop()
