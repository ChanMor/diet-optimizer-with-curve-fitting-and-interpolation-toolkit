from tkinter import *
import ttkbootstrap as ttk
from .polynomialRegression import PolynomialRegressionPage 
from .quadraticSplineInterpolation import QuadraticSplineInterpolationPage

class GenericSolverPage(ttk.Frame):
    def __init__(self, root, send_to, main_frame):
        super().__init__(root)
        generic_solver_label = ttk.Label(self, text="Generic Solver", font=("Arial", 28), bootstyle="default")
        generic_solver_label.pack(pady=50)

        self.polynomial_regression_frame = PolynomialRegressionPage(root, self.send_to, self)
        self.quadratic_spline_interpolation_frame = QuadraticSplineInterpolationPage(root, self.send_to, self)

        polynomial_regression_btn = ttk.Button(self, text="Polynomial Regression", bootstyle="light-outline", command=lambda: self.send_to(self.polynomial_regression_frame))
        polynomial_regression_btn.pack(pady=20)

        quadratic_spline_interpolation_btn = ttk.Button(self, text="Quadratic Spline Interpolation", bootstyle="light-outline", command=lambda: self.send_to(self.quadratic_spline_interpolation_frame))
        quadratic_spline_interpolation_btn.pack(pady=20)

        back_btn = ttk.Button(self, text="Back", bootstyle="light-outline", command=lambda: send_to(main_frame))
        back_btn.pack(pady=20)
    
    def send_to(self, page_to_show):
        for frame in [self, self.polynomial_regression_frame, self.quadratic_spline_interpolation_frame]:
            if frame == page_to_show:
                page_to_show.pack()
            else:
                frame.pack_forget()