import numpy as np
from simplex_method_util import simplex_method

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
    if foods == []:
        print("System: No Food Selected!")
        return None


    simplex_matrix = simplex_method(foods)

    if simplex_matrix is None:
        return None

    solution_array = generate_solution_array(simplex_matrix)

    rounded_solution_array = np.round(solution_array, decimals=2)
    food_dict = dict(zip(foods, rounded_solution_array))
    
    return food_dict

selected_foods = ["Frozen Broccoli", "Carrots Raw", "Celery Raw", "Frozen Corn",
            "Lettuce, Iceberg, Raw", "Peppers, Sweet, Raw", "Potatoes, Baked",
            "Tofu", "Roasted Chicken", "Spaghetti W/ Sauce",
            "Tomato, Red, Ripe, Raw", "Apple, Raw, W/ Skin", "Banana", "Grapes",
            "Kiwifruit, Raw, Fresh", "Oranges", "Bagels", "Wheat Bread",
            "White Bread", "Oatmeal Cookies", "Apple Pie",
            "Chocolate Chip Cookies", "Butter, Regular", "Cheddar Cheese",
            "3.3'%' Fat, Whole Milk", "2'%' Lowfat Milk", "Skim Milk",
            "Poached Eggs", "Scrambled Eggs", "Bologna, Turkey",
            "Frankfurter, Beef", "Ham, Sliced, Extralean", "Kielbasa, Prk",
            "Cap'N Crunch", "Cheerios", "Corn Flks, Kellog'S",
            "Raisin Brn, Kellg'S", "Rice Krispies", "Special K", "Oatmeal",
            "Malt-O-Meal, Choc", "Pizza W/ Pepperoni", "Taco",
            "Hamburger W/ Toppings", "Hotdog, Plain", "Couscous",
            "White Rice", "Macaroni, Ckd", "Peanut Butter", "Pork",
            "Sardines in Oil", "White Tuna in Water", "Popcorn, Air-Popped",
            "Potato Chips, Bbqflvr", "Tortilla Chip", "Chicknoodl Soup",
            "Splt Pea&Hamsoup", "Vegetbeef Soup", "Neweng Clamchwd",
            "Tomato Soup", "New E Clamchwd, W/ Mlk", "Crm Mshrm Soup, W/ Mlk",
            "Beanbacn Soap, W/ Watr"]
print(selected_foods)
print(generate_dictionary(selected_foods))