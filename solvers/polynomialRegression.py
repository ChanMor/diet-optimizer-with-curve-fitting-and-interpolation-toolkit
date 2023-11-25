from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk
from util.polynomialRegressionUtil import *

class PolynomialRegressionPage(ttk.Frame):
    def __init__(self, root, send_to, generic_solver):
        super().__init__(root)
        self.file_x = StringVar()
        self.file_y = StringVar()
        self.file = StringVar()

        polynomial_regression_label = ttk.Label(self, text="Polynomial Regression Solver", font=("Arial", 28), bootstyle="default")
        polynomial_regression_label.grid(row=0, column=0, columnspan=4, pady=10)

        page_title_separator = ttk.Separator(self, orient='horizontal', style='secondary.Horizontal.TSeparator')
        page_title_separator.grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

        back_btn = ttk.Button(self, text="Back", bootstyle="light-outline", command=lambda: send_to(generic_solver))
        back_btn.grid(row=2, column=1, pady=10, sticky="w")

        self.result_canvas = ttk.Canvas(self, width=400, height=100, bg='white')
        self.result_canvas.grid(row=3, rowspan=4, column=2, columnspan=2, sticky="w")

        degree_label = ttk.Label(self, text="Degree:")
        degree_label.grid(row=3, column=1, pady=10, sticky="w")

        self.degree_entry = ttk.Entry(self, width=40)
        self.degree_entry.grid(row=4, column=1, columnspan=3, pady=10, padx=10, sticky="w")

        data_label_x = ttk.Label(self, text="Data Points X (comma-separated or CSV file):")
        data_label_x.grid(row=5, column=1, pady=10, sticky="w")

        self.data_entry_x = ttk.Entry(self, textvariable=self.file_x, width=40)
        self.data_entry_x.grid(row=6, column=1, columnspan=3, pady=10, padx=10, sticky="w")

        data_label_y = ttk.Label(self, text="Data Points Y (comma-separated or CSV file):")
        data_label_y.grid(row=7, column=1, pady=10, sticky="w")

        self.data_entry_y = ttk.Entry(self, textvariable=self.file_y, width=40)
        self.data_entry_y.grid(row=8, column=1, columnspan=3, pady=10, padx=10, sticky="w")

        estimate_label = ttk.Label(self, text="Estimate: ")
        estimate_label.grid(row=9, column=1, pady=10, sticky="w")

        self.estimate_entry = ttk.Entry(self, width=40)
        self.estimate_entry.grid(row=10, column=1, columnspan=3, pady=10, padx=10, sticky="w")

        upload_csv_btn = ttk.Button(self, text="Upload CSV file", bootstyle="light-outline", command=self.browse_csv)
        upload_csv_btn.grid(row=11, column=1, pady=10, padx=10, sticky="w")

        calculate_btn = ttk.Button(self, text="Calculate", bootstyle="primary", command=self.calculate_polynomial)
        calculate_btn.grid(row=11, column=1, pady=10, padx=160, sticky="w")

        reset_btn = ttk.Button(self, text="Reset", bootstyle="danger", command=self.reset)
        reset_btn.grid(row=11, column=1, pady=10, padx=275, sticky="w")

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

        self.degree_entry.delete(0, END)
        self.data_entry_x.delete(0, END)
        self.data_entry_y.delete(0, END)
        self.estimate_entry.delete(0, END)
        
        self.result_canvas.delete("all")

    def calculate_polynomial(self):
        try:
            degree = int(self.degree_entry.get())

            if self.file_y.get() == "CSV file successfully uploaded":
                data = self.load_csv_data()
            else: 
                data = self.load_entry_data()

            estimate_data = float(self.estimate_entry.get())

            result = get_polynomial_regression_function(degree, data)
            estimate_result = estimate_polynomial_regression(degree, data, estimate_data)
            
            self.result_canvas.delete("all")
            self.result_canvas.create_text(10, 10, anchor="nw", text=f"Polynomial Function: {result}\nEstimate at {estimate_data}: {estimate_result}", width=380, fill="lightgrey")

        except ValueError:
            self.result_canvas.delete("all")
            self.result_canvas.create_text(10, 10, anchor="nw", text="Invalid input. Please check your input values.", width=380, fill="lightcoral")
