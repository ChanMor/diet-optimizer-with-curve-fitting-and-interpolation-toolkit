import numpy as np

from tkinter import *
import ttkbootstrap as ttk

class MatrixDisplay(ttk.Frame):
    def __init__(self, root, matrix, selected_foods):
        super().__init__(root)
        self.selected_foods = selected_foods
        self.matrix = matrix

        self.initialize_frame()

    def initialize_frame(self):
        self.generate_column_names()
        self.generate_simplex_iteration_frame()
        self.generate_simplex_basic_solution_frame()

    def generate_column_names(self):
        self.columns_names = [f"S{i+1}" for i in range(self.matrix.shape[1] - len(self.selected_foods) - 2)]
        self.columns_names.extend([f"x{i+1}" for i in range(len(self.selected_foods))])
        self.columns_names.extend(["z", "RHS"])

    def generate_simplex_iteration_frame(self):
        simplex_iteration_frame = ttk.Frame(self)
        simplex_iteration_frame.pack(padx=130, pady=10)

        simplex_iteration_y_scrollbar = ttk.Scrollbar(simplex_iteration_frame, bootstyle="dark-round")
        simplex_iteration_y_scrollbar.pack(side="right", fill="y")

        simplex_iteration_x_scrollbar = ttk.Scrollbar(simplex_iteration_frame, orient="horizontal", bootstyle="dark-round")
        simplex_iteration_x_scrollbar.pack(side="bottom", fill="x")

        simplex_iteration_treeview = ttk.Treeview(simplex_iteration_frame, columns=self.columns_names, show="headings",  yscrollcommand=simplex_iteration_y_scrollbar.set, xscrollcommand=simplex_iteration_x_scrollbar.set, height=15, bootstyle="dark")
        
        for column_name in self.columns_names:
            simplex_iteration_treeview.heading(column_name, text=column_name, anchor="w")
            simplex_iteration_treeview.column(column_name, width=50)

        for i in range(self.matrix.shape[0]):
            row_values = tuple(np.round(self.matrix[i, :], decimals=4))
            simplex_iteration_treeview.insert("", "end", values=row_values)

        simplex_iteration_y_scrollbar.config(command=simplex_iteration_treeview.yview)
        simplex_iteration_x_scrollbar.config(command=simplex_iteration_treeview.xview)

        simplex_iteration_treeview.pack()

    def generate_simplex_basic_solution_frame(self):
        simplex_basic_solution_frame = ttk.Frame(self)
        simplex_basic_solution_frame.pack(padx=130, pady=20)

        simplex_basic_solution_x_scrollbar = ttk.Scrollbar(simplex_basic_solution_frame, orient="horizontal", bootstyle="dark-round")
        simplex_basic_solution_x_scrollbar.pack(side="bottom", fill="x")

        simplex_iteration_treeview = ttk.Treeview(simplex_basic_solution_frame, columns=self.columns_names, show="headings", xscrollcommand=simplex_basic_solution_x_scrollbar.set, height=1, bootstyle="dark")
        
        for column_name in self.columns_names:
            simplex_iteration_treeview.heading(column_name, text=column_name, anchor="w")
            simplex_iteration_treeview.column(column_name, width=50)

        simplex_iteration_treeview.insert("", "end", values=tuple(np.round(self.matrix[-1, :], decimals=4)))

        simplex_basic_solution_x_scrollbar.config(command=simplex_iteration_treeview.xview)

        simplex_iteration_treeview.pack()        
