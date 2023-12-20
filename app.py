from tkinter import *
import ttkbootstrap as ttk
from texts import *

from frames.diet_optimizer import DietOptimizerPage
from frames.polynomial_regression import PolynomialRegressionPage
from frames.quadratic_spline_interpolation import QuadraticSplineInterpolationPage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CMSC 150 Project")
        self.root.geometry("1280x820")
    
        self.frames = []
        self.initialize_frames()
    
    def initialize_frames(self):
        self.main_frame = self.generate_main_frame()
        self.main_frame.pack()

        self.generate_project_details()
        self.generate_diet_solver_content()
        self.generate_polynomial_regression_content()
        self.generate_quadratic_spline_interpolation_content()

        self.diet_optimizer_frame = DietOptimizerPage(self.root, self.send_to, self.main_frame)
        self.polynomial_regression_frame = PolynomialRegressionPage(self.root, self.send_to, self.main_frame)
        self.quadratic_spline_interpolation_frame = QuadraticSplineInterpolationPage(self.root, self.send_to, self.main_frame)

        self.frames.append(self.main_frame)
        self.frames.append(self.diet_optimizer_frame)
        self.frames.append(self.polynomial_regression_frame)
        self.frames.append(self.quadratic_spline_interpolation_frame)
        
    def generate_main_frame(self):
        main_frame = ttk.Frame(self.root)
        return main_frame
    
    def generate_project_details(self):
        self.project_frame = ttk.Frame(self.main_frame)

        project_title_label = ttk.Label(self.project_frame, text=project_title, font=("Arial Black", 28))
        project_title_label.pack(side="top", anchor="w", pady=15)

        project_description_label = ttk.Label(self.project_frame, text=project_description, font=("Bahnschrift Light", 11), wraplength=800, justify="left")
        project_description_label.pack(side="top", anchor="w")

        self.project_frame.pack(padx=130, pady=10, fill="both", expand=True)

    def generate_diet_solver_content(self):
        self.diet_solver_content_frame = ttk.Frame(self.main_frame)

        diet_solver_button = ttk.Button(self.diet_solver_content_frame, text=diet_solver_button_text, bootstyle="outline.light", command=lambda: self.send_to(self.diet_optimizer_frame))
        diet_solver_button.pack(side="top", anchor="w", pady=10)

        diet_solver_description_label = ttk.Label(self.diet_solver_content_frame, text=diet_solver_description, font=("Bahnschrift Light", 11), wraplength=800, justify="left")
        diet_solver_description_label.pack(side="top", anchor="w")

        self.diet_solver_content_frame.pack(padx=130, pady=10, fill="both", expand=True)

    def generate_polynomial_regression_content(self):
        self.polynomial_regression_content_frame = ttk.Frame(self.main_frame)

        polynomial_regression_button = ttk.Button(self.polynomial_regression_content_frame, text=polynomial_regression_button_text, bootstyle="outline.light", command=lambda: self.send_to(self.polynomial_regression_frame))
        polynomial_regression_button.pack(side="top", anchor="w", pady=10)

        polynomial_regression_description_label = ttk.Label(self.polynomial_regression_content_frame, text=polynomial_regression_description, font=("Bahnschrift Light", 11), wraplength=800, justify="left")
        polynomial_regression_description_label.pack(side="top", anchor="w")

        self.polynomial_regression_content_frame.pack(padx=130, pady=10, fill="both", expand=True)

    def generate_quadratic_spline_interpolation_content(self):
        self.quadratic_spline_interpolation_content_frame = ttk.Frame(self.main_frame)

        quadratic_spline_interpolation_button = ttk.Button(self.quadratic_spline_interpolation_content_frame, text=quadratic_spline_interpolation_button_text, bootstyle="outline.light", command=lambda: self.send_to(self.quadratic_spline_interpolation_frame))
        quadratic_spline_interpolation_button.pack(side="top", anchor="w", pady=10)

        quadratic_spline_interpolation_description_label = ttk.Label(self.quadratic_spline_interpolation_content_frame, text=quadratic_spline_interpolation_description, font=("Bahnschrift Light", 11), wraplength=800, justify="left")
        quadratic_spline_interpolation_description_label.pack(side="top", anchor="w")

        self.quadratic_spline_interpolation_content_frame.pack(padx=130, pady=10, fill="both", expand=True)

    def send_to(self, page_to_show):
        for frame in self.frames:
            if frame == page_to_show:
                page_to_show.pack()
            else:
                frame.pack_forget()