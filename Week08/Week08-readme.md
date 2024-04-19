# Normal Distribution Histogram and Function Plotter

## Description
This Python script generates a histogram of a normal distribution and plots a function "( h(x) = x^3 \)" on the same set of axes using matplotlib and numpy.

## Usage
1. Run the script using a Python interpreter.
2. The script will generate a histogram of 1000 values from a normal distribution and plot the function \( h(x) = x^3 \) in the range 0 to 10.
3. The plot will be displayed on the screen.

## Details
- The script imports numpy and matplotlib libraries to generate the plot.
- It generates 1000 values from a normal distribution with a specified mean and standard deviation using numpy's `random.normal` function.
- A histogram of the generated values is created using matplotlib's `hist` function.
- The script generates values for the function \( h(x) = x^3 \) in the range 0 to 10 using numpy's `linspace` function.
- The function \( h(x) = x^3 \) is plotted on the sa
- The plot is displayed on the screen using matplotlib's `show` function.

## Notes
- This script shows data visualization techniques using matplotlib to create a histogram and plot a function on the same set of axes.
- It provides an example of how to combine different types of plots for data analysis and visualization purposes.