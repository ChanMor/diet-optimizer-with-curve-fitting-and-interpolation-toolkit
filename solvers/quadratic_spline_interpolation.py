from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk

from util.quadratic_spline_interpolation_util import *

class QuadraticSplineInterpolationPage(ttk.Frame):
    def __init__(self, root, send_to, generic_solver):
        super().__init__(root)
        self.file_x = StringVar()
        self.file_y = StringVar()
        self.file = StringVar()

        polynomial_regression_label = ttk.Label(self, text="Quadratic Spline Interpolation Solver", font=("Arial", 28), bootstyle="default")
        polynomial_regression_label.pack(pady=20, anchor="w")

        page_title_separator = ttk.Separator(self, orient='horizontal', style='secondary.Horizontal.TSeparator')
        page_title_separator.pack(fill="both", expand=True)

        frame_right = ttk.Frame(self)
        frame_right.pack(side="right", padx=10)

        self.result_canvas = ttk.Canvas(frame_right, width=400, height=300, bg='white')
        self.result_canvas.pack(side="top", pady=5)

        frame_left = ttk.Frame(self)
        frame_left.pack(side="left", padx=10)

        back_btn = ttk.Button(frame_left, text="Back", bootstyle="light-outline", command=lambda: send_to(generic_solver))
        back_btn.pack(pady=20, anchor="w")

        data_label_x = ttk.Label(frame_left, text="Data Points X (comma-separated or CSV file):")
        data_label_x.pack(pady=5, anchor="w")

        self.data_entry_x = ttk.Entry(frame_left, textvariable=self.file_x, width=40)
        self.data_entry_x.pack(pady=5)

        data_label_y = ttk.Label(frame_left, text="Data Points Y (comma-separated or CSV file):")
        data_label_y.pack(pady=5, anchor="w")

        self.data_entry_y = ttk.Entry(frame_left, textvariable=self.file_y, width=40)
        self.data_entry_y.pack(pady=5)

        estimate_label = ttk.Label(frame_left, text="Estimate: ")
        estimate_label.pack(pady=5, anchor="w")

        self.estimate_entry = ttk.Entry(frame_left, width=40)
        self.estimate_entry.pack(pady=5)

        upload_csv_btn = ttk.Button(frame_left, text="Upload CSV file", bootstyle="light-outline", command=self.browse_csv)
        upload_csv_btn.pack(side="left", pady=20)

        calculate_btn = ttk.Button(frame_left, text="Calculate", bootstyle="primary", command=self.calculate_splines)
        calculate_btn.pack(side="left", pady=5, padx=30)

        reset_btn = ttk.Button(frame_left, text="Reset", bootstyle="danger", command=self.reset)
        reset_btn.pack(side="left", pady=5)

    def browse_csv(self):
        self.data_entry_x.config(state="disabled")
        self.data_entry_y.config(state="disabled")
        filename = filedialog.askopenfilename(title="Select CSV file for Data Points X", filetypes=[("CSV files", "*.csv")])
        self.file_y.set("CSV file successfully uploaded")
        self.file_x.set("CSV file successfully uploaded")
        self.file.set(filename)

    def load_csv_data(self):
        try:
            with open(self.file.get(), "r") as file:
                content = file.read().strip().split('\n')
                x_values = [float(value) for value in content[0].split(",")]
                y_values = [float(value) for value in content[1].split(",")]

                return [x_values, y_values]
        except Exception as e:
            raise ValueError(f"Error loading data from CSV file: {e}")

    def load_entry_data(self):
        x_values = [float(value) for value in self.file_x.get().split(",")]
        y_values = [float(value) for value in self.file_y.get().split(",")]
        return [x_values, y_values]

    def reset(self):
        self.data_entry_x.config(state="normal")
        self.data_entry_y.config(state="normal")

        self.data_entry_x.delete(0, END)
        self.data_entry_y.delete(0, END)
        self.estimate_entry.delete(0, END)
        
        self.result_canvas.delete("all")

    def calculate_splines(self):
        try:
            if self.file_y.get() == "CSV file successfully uploaded":
                data = self.load_csv_data()
            else: 
                data = self.load_entry_data()

            estimate_data = float(self.estimate_entry.get())

            results = generate_functions_strings(data)[1]
            estimate_result = generate_estimate(data, estimate_data)
            
            self.result_canvas.delete("all")

            y_coordinate = 10  
            for i, function_string in enumerate(results, start=1):
                self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"[{i}] Function:   {function_string}\n", width=400, fill="lightgrey")
                y_coordinate += 20 

            if estimate_result is None:
                self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"Value to be estimated is outside the range of the given data points", width=400, fill="lightgrey")
                return

            y_coordinate += 20  
            self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"Estimate at {estimate_data}:\n {estimate_result}", width=400, fill="lightgrey")

        except ValueError:
            self.result_canvas.delete("all")
            self.result_canvas.create_text(10, 10, anchor="nw", text="Invalid input. Please check your input values.", width=400, fill="lightcoral")

