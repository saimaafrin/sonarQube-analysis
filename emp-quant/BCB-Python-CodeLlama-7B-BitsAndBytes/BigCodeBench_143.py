
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Define the equation and its solution
    eq = np.poly1d([2, 1])
    sol = eq.roots

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(eq, label='y=2x+1')
    ax.scatter(sol, eq(sol), c='g', marker='o', label='Solution')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    return ax

# Call the function and display the plot
ax = task_func()
plt.show()