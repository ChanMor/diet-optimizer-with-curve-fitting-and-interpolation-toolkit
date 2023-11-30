import numpy as np
import simplex__method_util as sm

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

def generate_dictionary(foods):
    simplex_matrix = sm.simplex_method(foods)
    solution_array = generate_solution_array(simplex_matrix)

    rounded_solution_array = np.round(solution_array, decimals=2)
    food_dict = dict(zip(foods, rounded_solution_array))
    
    return food_dict

# selected_foods = ["Frozen Broccoli", "Carrots Raw", "Celery Raw", "Frozen Corn", "Lettuce, Iceberg, Raw", 
#                   "Roasted Chicken", "Potatoes, Baked", "Tofu", "Peppers, Sweet, Raw", "Spaghetti W/ Sauce", 
#                   "Tomato, Red, Ripe, Raw", "Apple, Raw, W/ Skin", "Banana", "Grapes", "Kiwifruit, Raw, Fresh", 
#                   "Oranges", "Bagels", "Wheat Bread", "White Bread", "Oatmeal Cookies"]

# selected_foods = ["Wheat Bread", "White Bread", "Frozen Broccoli", "Roasted Chicken", "Oatmeal Cookies", "Potatoes, Baked", "Tofu"]

# generate_dictionary(selected_foods)