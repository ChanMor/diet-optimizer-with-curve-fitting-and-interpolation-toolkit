
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

    iteration_count = 0
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
            subtrahend_row = matrix[i, pivot_column_index]*matrix[pivot_row_index,:]
            matrix[i,:] -= subtrahend_row

        last_column = matrix[:-1,-1]
        iteration_count += 1

    print(f"Preprocessing Iteration: {iteration_count}")
    return matrix