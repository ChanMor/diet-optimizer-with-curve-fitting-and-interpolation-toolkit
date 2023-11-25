from tkinter import *
import ttkbootstrap as ttk
from app import App

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = App(root)
    root.mainloop()
