import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Create a label to display the time
label = tk.Label(root, font=('Arial', 50), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()
root.mainloop()
