import tkinter as tk
from tkinter import simpledialog, messagebox

def run_gui():
    root = tk.Tk()
    root.withdraw()  # Hide root window

    command = simpledialog.askstring("Arcii", "What can I do for you?")
    if command:
        messagebox.showinfo("Response", f"You said: {command}")
    else:
        messagebox.showwarning("Arcii", "No input provided.")

