from tkinter import *
import ttkbootstrap as ttk

class QuadraticSplineInterpolationPage(ttk.Frame):
    def __init__(self, root, send_to, generic_solver):
        super().__init__(root)
        quadratic_spline_interpolation_label = ttk.Label(self, text="Quadratic Spline Interpolation Solver", font=("Arial", 28), bootstyle="default")
        quadratic_spline_interpolation_label.pack(pady=50)

        back_btn = ttk.Button(self, text="Back", bootstyle="light-outline", command=lambda: send_to(generic_solver))
        back_btn.pack(pady=20)


