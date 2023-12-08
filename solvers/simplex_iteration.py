from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

from util.matrix_display_util import MatrixDisplay
from texts import *

class SimplexIteration(ScrolledFrame):
    def __init__(self, root, simplex_iteration, selected_foods, optimized_solution_frame):
        super().__init__(root)
        self.simplex_iteration = simplex_iteration
        self.selected_foods = selected_foods
        self.optimized_solution_frame = optimized_solution_frame

        self.initialize_frames()

    def initialize_frames(self):
        self.simplex_iteration_details_frame = ttk.Frame(self)
        self.simplex_iteration_details_frame.pack(pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)

        self.simplex_iteration_frame= ttk.Frame(self)
        self.simplex_iteration_frame.pack(pady=10)

        self.generate_simplex_iteration_details()
        self.generate_buttons()
        self.generate_simplex_iteration()

    def generate_simplex_iteration_details(self):
        simplex_iteration_title_label = ttk.Label(self.simplex_iteration_details_frame, text="Simplex Iterations", font=("Arial Black", 28))
        simplex_iteration_title_label.pack(pady=15, anchor="w")

        simplex_iteration_description_label = ttk.Label(self.simplex_iteration_details_frame, text=simplex_iteration_text, font=("Bahnschrift Light", 10), wraplength=800, justify="left")
        simplex_iteration_description_label.pack(pady=5, anchor="w")

    def generate_simplex_iteration(self):
        for matrix in self.simplex_iteration:
            matrix_display = MatrixDisplay(self, matrix, self.selected_foods)
            matrix_display.pack(pady=10)

    def generate_buttons(self):
        back_button = ttk.Button(self.button_frame, text="Back", bootstyle="light-outline", command=lambda: self.send_to_optimized_solution_frame())
        back_button.pack(anchor="w", padx=5)

    def send_to_optimized_solution_frame(self):
        self.optimized_solution_frame.pack()
        self.pack_forget()
