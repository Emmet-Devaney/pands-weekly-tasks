import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate 1000 values from a normal distribution
mean = 5
std_dev = 2
values = np.random.normal(mean, std_dev, 1000)

# Create histogram for normal distribution
plt.hist(values, bins=30, density=True, alpha=0.6, color='g', label='Normal Distribution')

# Generate values for the function h(x) = x^3
x = np.linspace(0, 10, 100)
y = x**3

# Plot the function h(x) = x^3
plt.plot(x, y, color='r', label='$h(x) = x^3$')

# Add legend and labels
plt.legend()
plt.xlabel('x')
plt.ylabel('Density / Function Value')

# Set plot title
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')

# Display the plot
plt.grid(True)
plt.show()