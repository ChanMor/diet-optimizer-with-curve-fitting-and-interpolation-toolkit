import numpy as np

def gauss_jordan_method(matrix):
    n = len(matrix)
    for i in range(n):
        if i != n - 1:
            pivot_position = np.argmax(np.abs(matrix[i:, i])) + i
            pivot_row = matrix[pivot_position, :]
            if pivot_row[i] == 0:
                return None
            matrix[i, :], matrix[pivot_position, :] = matrix[pivot_position, :], matrix[i, :].copy()

        matrix[i, :] /= matrix[i, i]
        for j in range(n):
            if i == j:
                continue
            normalized_row = matrix[j, i] * matrix[i, :]
            matrix[j, :] -= normalized_row

    return matrix[:, -1]

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

    formated_function_body = str(format(result[0], ".4f"))
    function_body = str(result[0])
    for i, coeff in enumerate(result[1:], start=1):
        function_body += f" + {str(coeff)}*x**{i}"
        formated_function_body += f" + {str(format(coeff, ".4f"))}*x**{i}"
    
    return function_body,  formated_function_body

def estimate_polynomial_regression(degree, datapoints, data):
    function_body = get_polynomial_regression_function(degree, datapoints)[0]

    polynomial_function = lambda x: eval(function_body)
    return polynomial_function(data)