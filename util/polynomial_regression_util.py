import numpy as np

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

    return matrix[:,-1]

def get_rhs(degree, datapoints):
    x = np.array(datapoints[0]) 
    y = np.array(datapoints[1])

    RHS = np.zeros(degree + 1)
    for i in range(degree + 1):
        summation = np.sum(x**i * y)
        RHS[i] = summation
    
    return RHS

def get_augmented_coefficients(degree, datapoints):
    x = np.array(datapoints[0]) 
    y = np.array(datapoints[1])

    augmented_coefficients = np.zeros((degree+1)**2)
    for i in range(degree + 1):
        for j in range(degree + 1):
            coeff = np.sum(x**(j + i))
            augmented_coefficients[i * (degree + 1) + j] = coeff

    return augmented_coefficients

def get_augmented_coefficient_matrix(degree, datapoints):
    RHS = get_rhs(degree, datapoints)
    RHS = RHS.reshape(-1, 1)

    augmented_coefficients = get_augmented_coefficients(degree, datapoints)
    aug_coefficient_matrix = np.reshape(augmented_coefficients, (degree + 1, degree + 1), order='F')

    aug_coefficient_matrix = np.hstack((aug_coefficient_matrix, RHS))
    return aug_coefficient_matrix

def get_function_coefficients(degree, datapoints):
    aug_coefficient_matrix = get_augmented_coefficient_matrix(degree, datapoints)
    coefficients = gauss_jordan_method(np.copy(aug_coefficient_matrix))

    return coefficients

def get_polynomial_regression_function(degree, datapoints):
    result = get_function_coefficients(degree, datapoints)

    formated_function_body = ""
    if result[0] != 0:
        formated_function_body += str(round(result[0], 4))

    function_body = str(result[0])
    for i, coeff in enumerate(result[1:], start=1):
        function_body += f" + {str(coeff)}*x**{i}"
        if coeff > 0.00001 or coeff < -0.00001:
            formated_function_body += f" + {str(round(coeff, 5))}*x**{i}"
    
    return function_body,  formated_function_body

def estimate_polynomial_regression(degree, datapoints, data):
    function_body = get_polynomial_regression_function(degree, datapoints)[0]
    polynomial_function = lambda x: eval(function_body)
    return polynomial_function(data)