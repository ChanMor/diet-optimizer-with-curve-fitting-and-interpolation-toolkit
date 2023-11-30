import numpy as np
import pandas as pd
from .augmented_matrix_util import generate_augmented_matrix
from .preprocessing_matrix_util import preprocessing, has_negative

def find_pivot_column(array):
    negative_indices = np.where(array < 0)[0]
    if negative_indices.size > 0:
        pivot_col = negative_indices[np.argmax(np.abs(array[negative_indices]))]
        return pivot_col
    return None

def get_test_ratio(array, solution_column):
    test_ratio = np.empty(len(array))
    for i in range(len(array)):
        if array[i] == 0:
            test_ratio[i] = None
        else:
            test_ratio[i] = solution_column[i]/array[i]
    return test_ratio

def find_pivot_row_index(array, solution_column):
    test_ratio = get_test_ratio(array, solution_column)
    min_positive_index = np.where(test_ratio == np.min(test_ratio[test_ratio > 0]))[0]
    return min_positive_index[0]

def simplex_method(constraints):
    matrix = generate_augmented_matrix(constraints)
    matrix = preprocessing(matrix)
    last_row = matrix[-1,:-1]
    while has_negative(last_row):
        last_row = matrix[-1,:-1]

        solution_column = matrix[:,-1]

        pivot_column_index = find_pivot_column(last_row)
        pivot_column = matrix[:, pivot_column_index]
    
        pivot_row_index = find_pivot_row_index(pivot_column, solution_column)
        matrix[pivot_row_index,:] /= matrix[pivot_row_index, pivot_column_index]

        number_of_rows = matrix.shape[0]
        for i in range(number_of_rows):
            if i == pivot_row_index:
                continue
            normalized_row = matrix[i, pivot_column_index]*matrix[pivot_row_index,:]
            matrix[i,:] -= normalized_row

    return matrix

def format_matrix(matrix, variables):
    column_names = variables.copy()
    column_names.extend(["RHS"])
    df = pd.DataFrame(matrix, columns= column_names)
    df.index +=1
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df)