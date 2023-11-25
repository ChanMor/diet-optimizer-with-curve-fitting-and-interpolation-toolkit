import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import sympy as sp

# Define the symbolic variable
x = sp.symbols('x')

# Define the function symbolically
f = x**2 + 3*x + 2  # Replace this with your function

# Convert the expression to a PNG image
sp.preview(f, viewer='file', filename='function_image.png', euler=False)
