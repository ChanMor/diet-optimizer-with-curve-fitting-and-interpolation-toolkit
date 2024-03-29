from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk

from util.quadratic_spline_interpolation_util import *
from texts import *

class QuadraticSplineInterpolationPage(ttk.Frame):
    def __init__(self, root, send_to_main, main_frame):
        super().__init__(root)
        self.root = root
        
        self.file_x = StringVar()
        self.file_y = StringVar()
        self.file = StringVar()

        self.send_to_main = send_to_main
        self.main_frame = main_frame

        self.initialize_frames()

    def initialize_frames(self):
        self.frame_top = ttk.Frame(self)
        self.frame_top.pack(side="top", padx=10, fill="x")

        self.frame_left = ttk.Frame(self)
        self.frame_left.pack(side="left", padx=10)

        self.frame_right = ttk.Frame(self)
        self.frame_right.pack(side="right", padx=10)

        self.generate_polynomial_regression_details()
        self.generate_entry()
        self.generate_buttons()
        self.generate_result()

    def generate_polynomial_regression_details(self):
        polynomial_regression_label = ttk.Label(self.frame_top, text="Quadratic Spline Interpolation", font=("Arial Black", 28))
        polynomial_regression_label.pack(pady=15, anchor="w")

        csv_file_format_label = ttk.Label(self.frame_top, text="CSV FILE FORMAT", font=("Bahnschrift SemiBold", 10))
        csv_file_format_label.pack(side="top", anchor="w")

        csv_input_format_label = ttk.Label(self.frame_top, text=csv_format_text, font=("Bahnschrift Light", 10))
        csv_input_format_label.pack(side="top", anchor="w")

        csv_example_button = ttk.Button(self.frame_top, text="     See Example     ", bootstyle="light-outline", command=self.generate_csv_format)
        csv_example_button.pack(side="left", pady=10, anchor="w")

    def generate_result(self):
        self.result_canvas = ttk.Canvas(self.frame_right, width=400, height=300, bg='white')
        self.result_canvas.pack(side="top", pady=5)

    def generate_entry(self):
        self.entry_frame = ttk.Frame(self.frame_left)

        data_label_x = ttk.Label(self.frame_left, text="Data Points X (comma-separated or CSV file):")
        data_label_x.pack(pady=5, anchor="w")

        self.data_entry_x = ttk.Entry(self.frame_left, textvariable=self.file_x, width=40)
        self.data_entry_x.pack(pady=5)

        data_label_y = ttk.Label(self.frame_left, text="Data Points Y (comma-separated or CSV file):")
        data_label_y.pack(pady=5, anchor="w")

        self.data_entry_y = ttk.Entry(self.frame_left, textvariable=self.file_y, width=40)
        self.data_entry_y.pack(pady=5)

        estimate_label = ttk.Label(self.frame_left, text="Estimate: ")
        estimate_label.pack(pady=5, anchor="w")

        self.estimate_entry = ttk.Entry(self.frame_left, width=40)
        self.estimate_entry.pack(pady=5)

        self.entry_frame.pack()

    def generate_buttons(self):
        button_frame = ttk.Frame(self.frame_left)

        back_button = ttk.Button(button_frame, text="Back", bootstyle="light-outline", command=lambda: self.send_to_main(self.main_frame))
        back_button.pack(side="left", pady=5, padx=5)

        upload_csv_button = ttk.Button(button_frame, text="Upload CSV", bootstyle="light-outline", command=self.browse_csv)
        upload_csv_button.pack(side="left", pady=5, padx=5)

        calculate_button = ttk.Button(button_frame, text="Calculate", bootstyle="primary", command=self.calculate_splines)
        calculate_button.pack(side="left", pady=5, padx=5)

        reset_button = ttk.Button(button_frame, text="Reset", bootstyle="danger", command=self.reset)
        reset_button.pack(side="left", pady=5, padx=5)

        button_frame.pack()

    def generate_csv_format(self):
        csv_format_window = ttk.Toplevel(self.root)
        csv_format_window.title("CSV Format")
        csv_format_window.geometry("200x300")

        x_values = [1, 4, 6, 7, 8, 11, 15]
        y_values = [10.00, 25.00, 33.50, 15.75, 28.00, 34.02, 30.00]

        values_frame = ttk.Frame(csv_format_window)
        values_frame.pack(pady=10)

        csv_format_label = ttk.Label(values_frame, text="CSV File Format", font=("Bahnschrift Light", 10))
        csv_format_label.pack(pady=10)

        data_label = ttk.Label(values_frame, text="     x   ,\t  y", font=("Aptos", 10))
        data_label.pack(anchor="w", pady=5)

        for x, y in zip(x_values, y_values):
            data_label = ttk.Label(values_frame, text=f"    {format(x, "02d")}  ,\t{format(y, ".2f")}", font=("Aptos", 10))
            data_label.pack(anchor="w", pady=2)

    def browse_csv(self):
        self.data_entry_x.config(state="disabled")
        self.data_entry_y.config(state="disabled")
        filename = filedialog.askopenfilename(title="Select CSV file for Data Points X", filetypes=[("CSV files", "*.csv")])
        self.file_y.set("CSV file successfully uploaded")
        self.file_x.set("CSV file successfully uploaded")
        self.file.set(filename)

    def load_csv_data(self):
        try:

            x_values = []
            y_values = []
            
            with open(self.file.get(), "r") as file:
                lines = file.read().strip().split('\n')
                data = [list(map(float, line.split(","))) for line in lines]

                data.sort(key=lambda pair: pair[0])
                x_values, y_values = zip(*data)

            return [list(x_values), list(y_values)]
        
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

            if len(data[0]) != len(data[1]):
                self.error()
                return

            estimate_data = float(self.estimate_entry.get())

            if estimate_data > data[0][-1] or estimate_data < data[0][0]:
                self.error()
                return

            results = generate_functions_strings(data)[1]
            estimate_result = generate_estimate(data, estimate_data)
            
            self.result_canvas.delete("all")

            y_coordinate = 10  
            for i, function_string in enumerate(results, start=1):
                self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"[{i}] Function:   {function_string.replace("**", "^")}\n", width=400, fill="lightgrey")
                y_coordinate += 20 

            if estimate_result is None:
                self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"Value to be estimated is outside the range of the given data points", width=400, fill="lightgrey")
                return

            y_coordinate += 20  
            self.result_canvas.create_text(10, y_coordinate, anchor="nw", text=f"Estimate at {estimate_data}:\n {format(estimate_result, ".4f")}", width=400, fill="lightgrey")

        except ValueError:
            print("wtf")
            self.error()
            
    def error(self):
        self.result_canvas.delete("all")
        self.result_canvas.create_text(10, 10, anchor="nw", text="Invalid input. Please check your input values.", width=400, fill="lightcoral")
