import tkinter as tk
from tkinter import messagebox, ttk
import time


def start_processing():
    # Get the number from the Entry widget
    user_number = number_entry.get()

    # Check if the user number is a valid integer
    if not user_number.isdigit():
        messagebox.showerror("Error", "Please enter a valid integer.")
        return

    # Disable the button to prevent multiple clicks
    process_button.config(state=tk.DISABLED)

    # Create a new pop-up window
    progress_window = tk.Toplevel(root)
    progress_window.title("Processing")

    # Create a label for the progress status
    progress_label = tk.Label(progress_window, text="Starting...")
    progress_label.pack()

    # Create a Progress Bar
    progress_bar = ttk.Progressbar(progress_window, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack()

    progress_window.update()

    # Simulate a long process with the progress bar
    for i in range(1, 101):
        progress_label.config(text=f"Analyzing... Making prediction ({i}%)")
        progress_bar['value'] = i
        progress_window.update()
        time.sleep(0.05)  # simulate some processing time

    # Close the progress window
    progress_window.destroy()

    # Re-enable the button
    process_button.config(state=tk.NORMAL)

    # Show the result in a message box
    messagebox.showinfo("Prediction", f"The number you entered is {user_number}")


# Create the main window
root = tk.Tk()
root.title("Number Predictor")

# Create an Entry widget for the user to enter a number
number_label = tk.Label(root, text="Enter a number:")
number_label.pack()

number_entry = tk.Entry(root)
number_entry.pack()

# Create a Button to trigger the processing
process_button = tk.Button(root, text="Process", command=start_processing)
process_button.pack()

# Run the event loop
root.mainloop()