import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from util.food_data_util import foods

class DietSolverPage(ttk.Frame):
    def __init__(self, root, send_to, main_frame):
        super().__init__(root)
        self.root = root
        self.send_to = send_to
        self.main_frame = main_frame

        diet_solver_label = ttk.Label(self, text="Diet Solver", font=("Arial", 28), bootstyle="default")
        diet_solver_label.pack(pady=50)

        page_title_separator = ttk.Separator(self, orient='horizontal', style='secondary.Horizontal.TSeparator')
        page_title_separator.pack(fill="both", expand=True)

        self.foods = foods
        self.selected_foods = []

        self.checkbox_parent_frame = ttk.Frame(self)
        self.checkbox_parent_frame.pack(pady=20)

        checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
        checkbox_frame.pack(side="left", padx=5, pady=5)
        for i, food in enumerate(self.foods):
            checkbox_var = tk.BooleanVar(value=False)
            food_checkbox = ttk.Checkbutton(checkbox_frame, text=food, variable=checkbox_var, onvalue=True, offvalue=False,
                                            command=lambda f=food, var=checkbox_var: self.toggle_selection(f, var))
            food_checkbox.pack(side="top", pady=5, anchor="w")

            if (i + 1) % 9 == 0:
                checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
                checkbox_frame.pack(side="left", padx=5, pady=5)

        back_btn = ttk.Button(self, text="Back", bootstyle="light-outline", command=lambda: self.send_to(self.main_frame))
        back_btn.pack(side="left", pady=5, anchor="w")

        select_button = ttk.Button(self, text="Select", bootstyle="primary", command=self.select_foods)
        select_button.pack(side="left", pady=5, padx=10, anchor="w")

        clear_button = ttk.Button(self, text="Clear Selection", bootstyle="danger", command=self.clear_selection)
        clear_button.pack(side="left", pady=5, anchor="w")

    def toggle_selection(self, food, checkbox_var):
        selected = checkbox_var.get()
        if selected:
            self.selected_foods.append(food)
        else:
            self.selected_foods.remove(food)

    def select_foods(self):
        print("Selected Foods:", self.selected_foods)

    def clear_selection(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                frame.destroy()

        checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
        checkbox_frame.pack(side="left", padx=5, pady=5)
        for i, food in enumerate(self.foods):
            checkbox_var = tk.BooleanVar(value=False)
            food_checkbox = ttk.Checkbutton(checkbox_frame, text=food, variable=checkbox_var, onvalue=True, offvalue=False,
                                            command=lambda f=food, var=checkbox_var: self.toggle_selection(f, var))
            food_checkbox.pack(side="top", pady=5, anchor="w")

            if (i + 1) % 9 == 0:
                checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
                checkbox_frame.pack(side="left", padx=5, pady=5)

        self.selected_foods.clear()
        