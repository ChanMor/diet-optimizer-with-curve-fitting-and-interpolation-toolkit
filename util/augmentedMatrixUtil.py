import numpy as np

def get_right_hand_side(system):
    right_hand_side = []
    for eq in system:
        terms = eq.split("+")
        for term in terms:
            term_parts = term.split("*")
            if len(term_parts) == 1:
                coefficients = float(term_parts[0].strip())
                coefficients *= -1
                right_hand_side.append(coefficients)
    return np.array(right_hand_side)

def get_coefficients(variables, system):
    list_of_equations = np.copy(system)
    list_of_coefficients = []
    for var in variables:
        for eq in list_of_equations:
            terms = eq.split("+")
            for term in terms:
                term_parts = term.split("*")
                if len(term_parts) == 2 and term_parts[1].strip().startswith(var):
                    coefficients = float(term_parts[0].strip())
                    list_of_coefficients.append(coefficients)
    return (list_of_coefficients)

def get_augmented_coefficient_matrix(variables, system):
    var = variables
    num_of_columns = len(var)
    coefficients = get_coefficients(variables, system)
    RHS = get_right_hand_side(system)
    matrix = np.array(coefficients).reshape(-1, num_of_columns, order="F")
    matrix = np.column_stack((matrix, RHS))
    
    return matrix

