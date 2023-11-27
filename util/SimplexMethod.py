import numpy as np
np.set_printoptions(precision=2, suppress=True)

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
    print(solution_column)
    test_ratio = get_test_ratio(array, solution_column)
    min_positive_index = np.where(test_ratio == np.min(test_ratio[test_ratio > 0]))[0]
    return min_positive_index[0]

def find_identity(array):
    if 1 in array:
        instance_of_1 = np.where(array == 1)[0]
        if instance_of_1.size == 1:
            return instance_of_1.item()
        return instance_of_1[0].item()
    return None
    
def is_identity(array, index):
    for i in range(len(array)):
        if i == index:
            continue
        if array[i] != 0:
            return False
    return True

def get_solution(matrix):
    num_variables = matrix.shape[1] - 1
    solution = np.empty(num_variables)
    for i in range(num_variables):
        solution_index = find_identity(matrix[:, i])        
        if solution_index is not None and is_identity(matrix[:, i], solution_index):
            solution[i] = matrix[solution_index, -1]
        else:
            solution[i] = 0
    return solution

def has_negative(array):
    for coefficient in array:
        if coefficient < 0:
            return True
    return False

def preprocessing_pivot_row(array):
    index = 0
    for coefficient in array:
        if coefficient < 0:
            return index
        index += 1

def preprocessing_pivot_column(array):
    index = 0
    for coefficient in array:
        if coefficient < 0:
            return index
        index += 1

def preprocessing(matrix):
    last_column = matrix[:-1,-1]
    while has_negative(last_column):

        pivot_row_index = preprocessing_pivot_row(last_column)
        pivot_column_determinant = matrix[pivot_row_index, :]

        pivot_column_index = preprocessing_pivot_column(pivot_column_determinant)
        pivot_element = matrix[pivot_row_index, pivot_column_index]

        matrix[pivot_row_index,:] /= pivot_element
        
        number_of_rows = matrix.shape[0]
        for i in range(number_of_rows):
            if i == pivot_row_index:
                continue
            normalized_row = matrix[i, pivot_column_index]*matrix[pivot_row_index,:]
            matrix[i,:] -= normalized_row
        last_column = matrix[:-1,-1]
        
    return matrix

def simplex_method(constraints):
    #matrix = am.get_augmented_coefficient_matrix(constraints)
    matrix = np.copy(constraints)
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

# def E1(x1, x2, s1, s2, s3, z):
#     return -1 * x1 + -1 * x2 + 1 * s1 + 0 * s2 + 0 * s3 + 0 * z + 20

# def E2(x1, x2, s1, s2, s3, z):
#     return -1 * x1 + -2 * x2 + 0 * s1 + 1 * s2 + 0 * s3 + 0 * z + 25

# def E3(x1, x2, s1, s2, s3, z):
#     return -5 * x1 +  1 * x2 + 0 * s1 + 0 * s2 + 1 * s3 + 0 * z + -4

# def E4(x1, x2, s1, s2, s3, z):
#     return  3 * x1 +  4 * x2 + 0 * s1 + 0 * s2 + 0 * s3 + 1 * z + 0



# def E1(x1, x2, s1, s2, z):
#     return -1 * x1 + -2 * x2 + 1 * s1 + 0 * s2 + 0 * z + 4

# def E2(x1, x2, s1, s2, z):
#     return -7 * x1 + -6 * x2 + 0 * s1 + 1 * s2 + 0 * z + 20

# def E3(x1, x2, s1, s2, z):
#     return 14 * x1 +  20 * x2 + 0 * s1 + 0 * s2 + 1 * z + 0


# constraints = [E1, E2, E3]
# solution_matrix = simplex_method(constraints)
# print(solution_matrix)
# print(get_solution(solution_matrix))


