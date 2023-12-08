import tkinter as tk
from tkinter import ttk

def on_entry_click(event):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(foreground='black')

def on_entry_leave(event):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(foreground='grey')

root = tk.Tk()
root.title("Default Text in ttk.Entry")

default_text = "Enter your text here"

# Create and pack ttk.Entry
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, foreground='grey')
entry.insert(0, default_text)
entry.pack(pady=10)

# Bind events
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_entry_leave)

# Set default color
entry.config(foreground='grey')

root.mainloop()
