import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style

class NewWindowGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        # Create a ttkbootstrap style
        self.style = Style("lumen")

        # Create a button
        self.generate_button = ttk.Button(
            self.master,
            text="Generate New Window",
            command=self.generate_new_window
        )
        self.generate_button.pack(pady=20)

    def generate_new_window(self):
        # Create a new window
        new_window = ttk.Toplevel(self.master)
        new_window.title("New Window")

        # Add content to the new window
        label = ttk.Label(new_window, text="This is a new window!")
        label.pack(padx=20, pady=20)

# Create the main Tkinter window
root = tk.Tk()
app = NewWindowGenerator(root)
root.mainloop()
