from tkinter import *
from solvers.genericSolver import GenericSolverPage

import ttkbootstrap as ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CMSC 150 Project")
        self.root.geometry("1080x720")
    
        self.style = ttk.Style()
        self.is_dark_mode = False

        self.main_frame = self.create_main_page()
        self.generic_solver_frame = GenericSolverPage(root, self.send_to, self.main_frame)

        self.send_to(self.main_frame)
    
    def create_main_page(self):
        main_frame = ttk.Frame(self.root)
        main_label = ttk.Label(main_frame, text="Main Page", font=("Arial", 28), bootstyle="default")
        main_label.pack(pady=50)
    
        generic_solver_btn = ttk.Button(main_frame, text="Generic Solver", bootstyle="light-outline", command=lambda: self.send_to(self.generic_solver_frame))
        generic_solver_btn.pack(pady=20)

        mode_toggle_btn = ttk.Button(main_frame, text="Toggle Mode", style="light-outline", command=self.toggle_mode)
        mode_toggle_btn.pack(pady=20)

        return main_frame
    
    def send_to(self, page_to_show):
        for frame in [self.main_frame, self.generic_solver_frame]:
            if frame == page_to_show:
                page_to_show.pack()
            else:
                frame.pack_forget()

    def toggle_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        theme = "darkly" if self.is_dark_mode else "flatly"
        self.style.theme_use(theme)

        button_style = "light-outline" if self.is_dark_mode else "dark-outline"
        for frame in [self.main_frame]:
            for child in frame.winfo_children():
                if isinstance(child, ttk.Button):
                    child.configure(bootstyle=button_style)
