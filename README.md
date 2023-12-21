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
The program employs simplex method set up as a dual problem to solve for the optimal combination of foods.

## Polynomial Regression

Polynomial regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. This calculator employs polynomial regression to generate precise polynomial equations based on user-provided data points. Users can input their datasets and specify the desired polynomial degree, allowing the calculator to determine the optimal polynomial equation that best fits the given data. The result is an accurate polynomial equation that can be utilized for predictive purposes. This tool is invaluable for tasks where a more complex relationship between variables needs to be captured, offering a higher degree of accuracy in modeling. 


## Quadratic Spline Interpolation

The quadratic spline interpolation calculator employs quadratic functions to interpolate data points seamlessly within a given range. By utilizing quadratic polynomials for each interval, the calculator ensures both continuity and differentiability at the connection points, facilitating precise curve fitting for the provided dataset. This method optimally captures the underlying trends in the data, offering an accurate representation of the relationship between variables. The result is a smooth, continuous curve that accurately reflects the nuances of the dataset. Quadratic spline interpolation is particularly useful when dealing with real-world data that may exhibit non-linear patterns within specific ranges.

## Intalling External Modules

Make sure you have Python and pip installed on your system before running these commands. 
```bash
pip install tk
pip install ttkbootstrap
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
python3 main.py
```
