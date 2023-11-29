# CMSC 150 PYTHON PROJECT

An app that has a diet solver as its main features and generic solver as its additional feature. 
The diet solver involves the use of Simplex Method in minimization with mixed constraints. 
The generic solver on the other hand, has a feature to generate a polynomial regression function based on given data points
and another feature that involves quadratic spline interpolation.

## Diet Solver

The objective of this feature is to identify the most cost-effective and nutritious combination of foods that will fulfill all daily nutritional requirements. 
This problem is formulated as a linear program with the objectivem of minimizing cost under specified constraints and ensuring nutritional adequacy. 
These constraints control factors such as number of calories and amounts of vitamins, minerals, fats, sodium and cholesterol in the diet. 
Additionally, each food option is restricted to a range of 0-10 servings.

## Simplex Method for Minimization with Mixed Constraints

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
bash
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
