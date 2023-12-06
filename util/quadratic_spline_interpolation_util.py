import numpy as np

def generate_quadratic_polynomial_matrix(data):
    x_data = data[0]

    num_of_row = (len(x_data)*2)-2
    num_of_col = (len(x_data)-1)*3 

    quadratic_polynomial_matrix = np.zeros((num_of_row, num_of_col))
    for i in range(0, num_of_row, 2):
        j = int(i/2) * 3
        quadratic_polynomial_matrix[i, j:j + 3] = np.array([x_data[int(i/2)] ** 2, x_data[int(i/2)], 1])
        quadratic_polynomial_matrix[i+1, j:j + 3] = np.array([x_data[int(i/2) + 1] ** 2, x_data[int(i/2) + 1], 1])

    return quadratic_polynomial_matrix

def generate_continuous_derivative_matrix(data):
    x_data = data[0]

    num_of_col = (len(x_data)-1)*3 

    continuous_derivative_matrix = np.zeros((len(x_data)-2, num_of_col))
    for i in range(len(x_data)-2):
        continuous_derivative_array = np.array([x_data[i+1]*2, 1, 0, x_data[i+1]*-2, -1])
        continuous_derivative_matrix[i, i*3:i*3+5] = continuous_derivative_array

    return continuous_derivative_matrix

def generate_assumption_matrix(data):
    x_data = data[0]

    num_of_col = (len(x_data)-1)*3 

    assumption_matrix = np.zeros((1, num_of_col))
    assumption_matrix[0,0] = 1

    return assumption_matrix

def generate_right_hand_side(data, augmented_matrix):
    y_data = data[1]

    result_matrix = np.repeat(y_data[1:-1], 2)
    result_matrix = np.insert(result_matrix, 0, y_data[0])
    result_matrix = np.insert(result_matrix, 2*(len(y_data)-2)+1, y_data[len(y_data)-1])
   
    num_of_row = np.shape(augmented_matrix)[0]
    right_hand_side_matrix = np.zeros((num_of_row, 1))

    right_hand_side_matrix[0:2*(len(y_data)-2)+2,0] = result_matrix

    return right_hand_side_matrix

def generate_augmented_matrix(data):

    quadratic_polynomial_matrix = generate_quadratic_polynomial_matrix(data)
    continuous_derivative_matrix = generate_continuous_derivative_matrix(data)
    assumption_matrix = generate_assumption_matrix(data)

    augmented_matrix = np.vstack((quadratic_polynomial_matrix, continuous_derivative_matrix, assumption_matrix))
    right_hand_side_matrix = generate_right_hand_side(data, augmented_matrix)
    augmented_matrix = np.hstack((augmented_matrix, right_hand_side_matrix))

    return augmented_matrix

def gauss_jordan_method(matrix):

    num_of_row = matrix.shape[0]
    for i in range(num_of_row):

        if i != num_of_row - 1:
            pivot_row_index = np.argmax(np.abs(matrix[i:, i])) + i
            pivot_row = np.copy(matrix[pivot_row_index, :])
            
            if pivot_row[i] == 0:
                return None

            prev_pivot_row = matrix[i, :].copy()
            matrix[i, :] = pivot_row
            matrix[pivot_row_index, :] = prev_pivot_row
    
        matrix[i, :] /= matrix[i, i]
        for j in range(num_of_row):
            if i != j:   
                matrix[j, :] -= matrix[j, i] * matrix[i, :]
                
    return matrix

def generate_functions_strings(data):

    function_strings = []
    formated_function_strings = []

    augmented_matrix = generate_augmented_matrix(data)
    result_matrix = gauss_jordan_method(augmented_matrix)

    num_of_row = np.shape(result_matrix)[0]
    solution_array = result_matrix[:,-1]

    for i in range(0, num_of_row, 3):
        function_body = f"{solution_array[i]}*x**2 + {solution_array[i+1]}*x + {solution_array[i+2]}"
        formated_function_body = f"{format(solution_array[i], '.4f')}*x**2 + {format(solution_array[i+1], '.4f')}*x + {format(solution_array[i+2], '.4f')}"
        
        function_strings.append(function_body)
        formated_function_strings.append(formated_function_body)

    return function_strings, formated_function_strings


def generate_functions(function_strings):
    functions = []

    for functino_string in function_strings:
        function = lambda x, expression=functino_string: eval(expression)
        functions.append(function)

    return functions

def generate_estimate(data, estimate_input):
    function_strings = generate_functions_strings(data)[0]
    functions = generate_functions(function_strings)

    x_values = data[0]
    y_values = data[1]

    for i in range(len(x_values)-1):

        if estimate_input == x_values[i]:
            estimate_output = y_values[i]
            return estimate_output
        
        if estimate_input == x_values[i+1]:
            estimate_output = y_values[i+1]
            return estimate_output

        if estimate_input > x_values[i] and estimate_input < x_values[i+1]:
            function_index = i
            break

    estimate_output = functions[function_index](estimate_input)
    return estimate_output


x = [0, 10, 15, 20, 22.5, 30]
y = [0, 227.04, 362.78, 517.35, 602.97, 901.67]

data = [x,y]

print(generate_estimate(data, 16))