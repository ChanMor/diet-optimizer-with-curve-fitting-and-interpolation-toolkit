import tkinter as tk
from tkinter import *
from tkinter import ttk

from util.food_data_util import foods, food_cost
from util.generate_solution_util import generate_solution_dictionary

from texts import *

class DietOptimizerPage(ttk.Frame):
    def __init__(self, root, send_to, main_frame):
        super().__init__(root)
        self.root = root
        self.send_to = send_to
        self.main_frame = main_frame

        self.searched_food = StringVar()

        self.foods = foods
        self.food_cost = food_cost
        self.selected_foods = []

        self.initialize_frames()

    def initialize_frames(self):
        self.diet_optimizer_detail_frame = ttk.Frame(self)
        self.diet_optimizer_detail_frame.pack(side="top", padx=10, fill="x")

        self.checkbox_parent_frame = ttk.Frame(self)
        self.checkbox_parent_frame.pack(pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10, fill="x")

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(pady=10)

        self.generate_diet_optimizer_details()
        self.generate_food_checkbox()
        self.generate_buttons()


    def generate_diet_optimizer_details(self):
        diet_optimizer_title_label = ttk.Label(self.diet_optimizer_detail_frame, text="Diet Optimizer", font=("Arial Black", 28))
        diet_optimizer_title_label.pack(pady=15, anchor="w")

        self.generate_food_search()

    def generate_food_search(self):
        food_search_label = ttk.Label(self.diet_optimizer_detail_frame, text=food_search_description, font=("Bahnschrift Light", 10))
        food_search_label.pack(anchor="w")

        self.food_search_entry = ttk.Entry(self.diet_optimizer_detail_frame, textvariable=self.searched_food, width=40, foreground="grey", style="secondary.TEntry")
        self.food_search_entry.insert(0, "Search desired foods")
        self.food_search_entry.pack(side="left", anchor="w", pady=10)
        
        self.food_search_entry.bind('<FocusIn>', lambda event: self.on_entry_click())
        self.food_search_entry.bind('<FocusOut>', lambda event: self.on_entry_leave())

        self.add_food_button = ttk.Button(self.diet_optimizer_detail_frame, text="Add", bootstyle="light-outline", command=self.add_food)
        self.add_food_button.pack(side="left", anchor="w", padx=10, pady=10)

        self.success_promt = ttk.Label(self.diet_optimizer_detail_frame, text="")
        self.success_promt.pack(side="left", anchor="w", padx=10, pady=10)

    def generate_food_checkbox(self):
        checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
        checkbox_frame.pack(side="left", padx=5, pady=5)

        for i, food in enumerate(self.foods):

            checkbox_var = tk.BooleanVar(value=False)
            food_checkbox = ttk.Checkbutton(checkbox_frame, text=food, variable=checkbox_var, onvalue=True, offvalue=False, command=lambda f=food, var=checkbox_var: self.toggle_selection(f, var))
            food_checkbox.pack(side="top", pady=5, anchor="nw")

            if (i + 1) % 13 == 0:
                checkbox_frame = ttk.Frame(self.checkbox_parent_frame)
                checkbox_frame.pack(side="left", anchor="nw", padx=5, pady=5)

    def generate_buttons(self):
        back_btn = ttk.Button(self.button_frame, text="Back", bootstyle="light-outline", command=lambda: self.send_to(self.main_frame))
        back_btn.pack(side="left", anchor="w", padx=5)

        select_all_button = ttk.Button(self.button_frame, text="Select All", bootstyle="light-outline", command=self.select_all_foods)
        select_all_button.pack(side="left", anchor="w", padx=5)

        generate_button = ttk.Button(self.button_frame, text="Generate", bootstyle="primary", command=self.generate_optimal_solution)
        generate_button.pack(side="left", anchor="w", padx=5)

        clear_button = ttk.Button(self.button_frame, text="Clear Selection", bootstyle="danger", command=self.clear_selection)
        clear_button.pack(side="left", anchor="w", padx=5)

    def generate_optimal_solution(self):
        print(self.selected_foods)
        print("Selected Foods:", self.selected_foods)

        self.success_promt.config(text="")
        solution_dictionary = None
        if self.selected_foods != []:
            solution_dictionary = generate_solution_dictionary(self.selected_foods)

        print("Optimal Food Serving:", solution_dictionary)

    def on_entry_click(self):
        self.food_search_entry.delete(0, tk.END)

    def on_entry_leave(self):
        default_text = "Search desired food"
        entered_food = self.food_search_entry.get()

        if not entered_food or entered_food not in self.foods:
            self.food_search_entry.delete(0, tk.END)
            self.food_search_entry.insert(0, default_text)
            self.food_search_entry.config(foreground="grey")

    def add_food(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                for checkbox in frame.winfo_children():
                    if isinstance(checkbox, ttk.Checkbutton) and checkbox.cget("text") == self.food_search_entry.get():
                        checkbox.state(['selected'])

        self.generate_success_prompt()

    def generate_success_prompt(self):
        entered_food = self.food_search_entry.get()
        
        if entered_food in self.foods and entered_food not in self.selected_foods:
            self.success_promt.config(text=f"Succesfully added {self.food_search_entry.get()}", bootstyle="success")
            self.selected_foods.append(entered_food)

        elif entered_food in self.selected_foods:
            self.success_promt.config(text=f"{entered_food} is already selected", bootstyle="danger")
        elif entered_food == "Select desired food":
            self.success_promt.config(text="")
        else:
            self.success_promt.config(text=f"Food not in list of food selection", bootstyle="danger")

    def toggle_selection(self, food, checkbox_var):
        selected = checkbox_var.get()

        if selected:
            self.selected_foods.append(food)
        else:
            self.selected_foods.remove(food)

    def select_all_foods(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                for checkbox in frame.winfo_children():
                    if isinstance(checkbox, ttk.Checkbutton):
                        checkbox.state(['selected'])
                
        self.selected_foods.clear()
        for food in self.foods:
            self.selected_foods.append(food)

    def clear_selection(self):
        for frame in self.checkbox_parent_frame.winfo_children():
            if isinstance(frame, ttk.Frame):
                frame.destroy()

        self.generate_food_checkbox()
        self.selected_foods.clear()
        self.success_promt.config(text="")
        