import numpy as np
import pandas as pd

def generate_augmented_matrix(data):
    x_data = data[0]
    y_data = data[1]

    num_of_row = (len(x_data)*2)-2
    num_of_col = (len(x_data)-1)*3 

    quadratic_polynomial_matrix = np.zeros((num_of_row, num_of_col))
    for i in range(0, num_of_row, 2):
        j = int(i/2) * 3
        quadratic_polynomial_matrix[i, j:j + 3] = np.array([x_data[int(i/2)] ** 2, x_data[int(i/2)], 1])
        quadratic_polynomial_matrix[i+1, j:j + 3] = np.array([x_data[int(i/2) + 1] ** 2, x_data[int(i/2) + 1], 1])
    
    
    continuous_derivative_matrix = np.zeros((len(x_data)-2, num_of_col))
    for i in range(len(x_data)-2):
        continuous_derivative_array = np.array([x_data[i+1]*2, 1, 0, x_data[i+1]*-2, -1])

        continuous_derivative_matrix[i, i*3:i*3+5] = continuous_derivative_array

    last_equation_matrix = np.zeros((1, num_of_col))
    last_equation_matrix[0,0] = 1
    augmented_matrix = np.vstack((quadratic_polynomial_matrix, continuous_derivative_matrix, last_equation_matrix))

    rhs_num_of_row = np.shape(augmented_matrix)[0]
    rhs_matrix = np.zeros((rhs_num_of_row, 1))

    result_matrix = np.repeat(y_data[1:-1], 2)
    result_matrix = np.insert(result_matrix, 0, y_data[0])
    result_matrix = np.insert(result_matrix, 2*(len(y_data)-2)+1, y_data[len(y_data)-1])

    rhs_matrix[0:2*(len(y_data)-2)+2,0] = result_matrix

    augmented_matrix = np.hstack((augmented_matrix, rhs_matrix))

    df = pd.DataFrame(augmented_matrix)
    print(df)


def quadratic_spline_interpolation():
    pass

t = [0, 10, 15, 20, 22.5, 30]
v = [0, 227.04, 362.78, 517.35, 602.97, 901.67]

data = [t,v]

generate_augmented_matrix(data)