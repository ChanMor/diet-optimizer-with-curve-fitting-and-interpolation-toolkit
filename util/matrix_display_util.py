from numpy import *

from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

class MatrixDisplay(Frame):
    def __init__(self, root, matrix, selected_foods):
        super().__init__(root)
        self.selected_foods = selected_foods
        self.matrix = matrix

        self.initialize_frame()

    def initialize_frame(self):
        columns_names = [f"S{i+1}" for i in range(self.matrix.shape[1] - len(self.selected_foods) - 2)]
        columns_names.extend(self.selected_foods)
        columns_names.extend(["z", "Solution"])

        scrolled_frame_width = 800
        simplex_iteration_scrolled_frame = ScrolledFrame(self, width=scrolled_frame_width)
        simplex_iteration_scrolled_frame.pack(expand=True, fill='both')

        simplex_iteration_treeview = ttk.Treeview(simplex_iteration_scrolled_frame, columns=columns_names, show="headings", height=self.matrix.shape[0])
        simplex_iteration_treeview.pack(expand=True, fill='both')

        for column_name in columns_names:
            simplex_iteration_treeview.heading(column_name, text=column_name)

        for i in range(self.matrix.shape[0]):
            row_values = tuple(self.matrix[i, :])
            simplex_iteration_treeview.insert("", "end", values=row_values)
            
        simplex_iteration_bottom_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=simplex_iteration_treeview.xview)
        simplex_iteration_bottom_scrollbar.pack(side="bottom", fill=X)
        simplex_iteration_treeview.configure(xscrollcommand=simplex_iteration_bottom_scrollbar.set)

        