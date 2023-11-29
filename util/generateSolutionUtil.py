import numpy as np
import augmentedMatrixUtil as am
import SimplexMethodUtil as sm

def find_identity(array):
    if 1 in array:
        instance_of_1 = [i for i, value in enumerate(array) if value == 1]
        return instance_of_1[0]
    return None
    
def is_identity(array, index):
    for i in range(len(array)):
        if i == index:
            continue
        if array[i] != 0:
            return False
    return True

def generate_solution_array(matrix):
    num_variables = matrix.shape[1] - 1
    solution = np.empty(num_variables)
    for i in range(num_variables):
        solution_index = find_identity(matrix[:, i])        
        if solution_index is not None and is_identity(matrix[:, i], solution_index):
            solution[i] = matrix[solution_index, -1]
        else:
            solution[i] = 0
    return solution

selected_foods = ["Frozen Broccoli", "Carrots Raw", "Celery Raw", "Frozen Corn", "Lettuce, Iceberg, Raw", 
                  "Roasted Chicken", "Potatoes, Baked", "Tofu", "Peppers, Sweet, Raw", "Spaghetti W/ Sauce", 
                  "Tomato, Red, Ripe, Raw", "Apple, Raw, W/ Skin", "Banana", "Grapes", "Kiwifruit, Raw, Fresh", 
                  "Oranges", "Bagels", "Wheat Bread", "White Bread", "Oatmeal Cookies"]

variables = am.get_variables(selected_foods)
simplex_matrix = sm.simplex_method(selected_foods)
sm.format_matrix(simplex_matrix, variables)
print(generate_solution_array(simplex_matrix))