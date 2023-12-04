# CMSC 150 PYTHON PROJECT

An app that has a diet solver as its main features and generic solver as its additional feature. 
The diet solver involves the use of Simplex Method in minimization with mixed constraints. 
The generic solver on the other hand, has a feature to generate a polynomial regression function based on given data points
and another feature that involves quadratic spline interpolation.

## Diet Solver

The objective of this feature is to identify the most cost-effective and nutritious combination of foods that will fulfill all daily nutritional requirements.
The combination of foods will be based upon the food options selected by the user.
This problem is formulated as a linear program with the objectivem of minimizing cost under specified constraints and ensuring nutritional adequacy. 
These constraints control factors such as number of calories and amounts of vitamins, minerals, fats, sodium and cholesterol in the diet. 
Additionally, each food option is restricted to a range of 0-10 servings. 
The program employs simplex method minimization with mixed constraints to solve for the optimal combination of foods.


## Simplex Method for Minimization with Mixed Constraints

One technique to solve a mixed constraints minimization problem is to transform it to a simple 
maximization problem.

Setting Up the Matrix:

1. The <= constraints are retain in the augmented matrix normally
2. The >= constraints on the other hand are multiplied by -1 to convert it to  <= constraints
3. The objective function is multiplied by −1 to convert the it to a maximization problem

In this case, we are maximizing -f instead of f

Preprocessing the Matrix:

Since you cannot proceed with the simplex method while there is a negative in the last column there must be a preprocessing to eliminate the negatives in the last column

1. Pick any of the negative in last column and this will serve as the pivot row (exclude the last element in choosing a pivot row, as it would always be negative)
2. Choose any negative in the row and this will serve as the pivot element and the pivot column
3. Eliminate all rows similar to how you perform gauss jordan
4. Repeat until no negative exist in the last column

Simplex Method:

1. Choose the highest magnitude negative number in the last row and this will serve as the pivot column (exclude the last element in choosing a pivot row, as it would always be negative)
2. Find the smallest non negative test ratio (last column / pivot column), this will serve as the pivot row
3. Eliminate all rows similar to how you perform gauss jordan
4. Repeat until no negative exist in the last row
   
Reference:

[Simplex Method with Mixed Constraints](https://www.youtube.com/watch?v=YJLsXf9fcvw&t=491s&pp=ygUtc2ltcGxleCBtZXRob2QgbWluaW1pemF0aW9uIG1peGVkIGNvbnN0cmFpbnRz) | 
[Chapter 9 Linear Programming Mixed Constraints and Minimization](https://homepage.ntu.edu.tw/~jryanwang/courses/Mathematics%20for%20Management%20(undergraduate%20level)/Ch09_Text_Book.pdf?fbclid=IwAR2oCbAFUq9gh7AY2s9KcXbR975VVD1uAk5FZeYQyf1ovOXVRUtkKGTkTtw)

## Polynomial Regression

## Quadratic Spline Interpolation

## Intalling External Modules

Make sure you have Python and pip installed on your system before running these commands. 
```bash
pip install tk
pip install ttkbootstrap
pip install pandas
```
 If you're using a virtual environment, activate it before running the commands.
 ```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (Windows)
myenv\Scripts\activate

# Activate the virtual environment (Unix or MacOS)
source myenv/bin/activate
```
## Running the Program
Use the cd command to navigate to the directory:
```bash
cd path/to/your/script/directory
```
Once you are in the correct directory, run your Python script using the python command followed by the script's filename. For example:
```bash
python main.py
```
If you are using Python 3, you might need to use python3 instead:
```bash
python3 my_program.py
```
