import tkinter as tk
from tkinter import ttk
from util.food_data_util import foods, food_cost
from util.generate_solution_util import generate_dictionary
import math

class DietSolverPage(ttk.Frame):
    def __init__(self, root, send_to, main_frame):
        super().__init__(root)
        self.root = root
        self.send_to = send_to
        self.main_frame = main_frame

        self.foods = foods
        self.food_cost = food_cost
        self.selected_foods = []

        self.generate_labels()

        self.checkbox_parent_frame = ttk.Frame(self)
        self.checkbox_parent_frame.pack(pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10, fill="x")

        self.generate_food_checkbox()
        self.generate_buttons()

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(pady=10)

    def generate_labels(self):
        diet_solver_label = ttk.Label(self, text="Diet Solver", font=("Arial", 28), bootstyle="default")
        diet_solver_label.pack(pady=20)

    def generate_buttons(self):
        back_btn = ttk.Button(self.button_frame, text="Back", bootstyle="light-outline", command=lambda: self.send_to(self.main_frame))
        back_btn.pack(side="left", anchor="w")

        select_button = ttk.Button(self.button_frame, text="Generate", bootstyle="primary", command=self.generate)
        select_button.pack(side="left", padx=10, anchor="w")

        select_all_button = ttk.Button(self.button_frame, text="Select All", bootstyle="primary", command=self.select_all_foods)
        select_all_button.pack(side="left", padx=10, anchor="w")

        clear_button = ttk.Button(self.button_frame, text="Clear Selection", bootstyle="danger", command=self.clear_selection)
        clear_button.pack(side="left", anchor="w")

    def generate_food_checkbox(self):
        checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
        checkbox_frame.pack(side="left", padx=5, pady=5)

        for i, food in enumerate(self.foods):

            checkbox_var = tk.BooleanVar(value=False)
            food_checkbox = ttk.Checkbutton(checkbox_frame, text=food, variable=checkbox_var, onvalue=True, offvalue=False, command=lambda f=food, var=checkbox_var: self.toggle_selection(f, var))
            food_checkbox.pack(side="top", pady=5, anchor="w")

            if (i + 1) % 9 == 0:
                checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
                checkbox_frame.pack(side="left", padx=5, pady=5)

    def toggle_selection(self, food, checkbox_var):
        selected = checkbox_var.get()

        if selected:
            self.selected_foods.append(food)
        else:
            self.selected_foods.remove(food)

    def generate(self):
        print("Selected Foods:", self.selected_foods)

        for table in self.table_frame.winfo_children():
            if isinstance(table, ttk.Treeview):
                table.destroy()

        solution_dictionary = None
        if (self.selected_foods != []):
            solution_dictionary = generate_dictionary(self.selected_foods)

        self.display_foods(solution_dictionary)
        print("Optimal Food Serving:", solution_dictionary)

    def complete_food_selection(self):
        self.selected_foods.clear()
        for food in self.foods:
            self.selected_foods.append(food)

    def selected_state(self, frame):
        for checkbox in frame.winfo_children():
            if isinstance(checkbox, ttk.Checkbutton):
                checkbox.state(['selected'])

    def select_all_foods(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                self.selected_state(frame)
                
        self.complete_food_selection()

    def display_foods(self, food_dictionary):

        if food_dictionary is None:
            return None

        table = ttk.Treeview(self.table_frame, columns=("Foods", "Serving", "Cost"), show="headings")
        table.heading("Foods", text="Foods")
        table.heading("Serving", text="Serving")
        table.heading("Cost", text="Cost")
        table.pack(pady=10)

        for i, (food, serving) in enumerate(food_dictionary.items()):
            if serving == 0:
                continue
            
            if food == "Total Cost":
                table.insert(parent="", index=i, values=("Total Cost", "", format(serving, ".2f")))
                continue

            if not (len(food) == 2 or len(food) == 3):
                data = (food, format(serving, ".2f"), format(serving*self.food_cost[food], ".2f"))
                table.insert(parent="", index=i, values=data)


    def clear_selection(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                frame.destroy()

        self.generate_food_checkbox()
        self.selected_foods.clear()
        