from datetime import datetime
import random
import matplotlib.pyplot as plt
def task_func(
    epoch_milliseconds,
    teams=["Team1", "Team2", "Team3", "Team4", "Team5"],
    random_seed=0,
):
    # Convert epoch milliseconds to datetime
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    # Get today's date
    end_date = datetime.now()
    # Calculate the number of days between start and end date
    num_days = (end_date - start_date).days + 1
    
    # Initialize a dictionary to store performance data
    performance_data = {team: [] for team in teams}
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random performance data for each team for each day
    for day in range(num_days):
        for team in teams:
            performance = random.uniform(0.1, 1)
            performance_data[team].append(performance)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the performance data for each team
    for team, data in performance_data.items():
        ax.plot(range(num_days), data, label=team)
    
    # Set the labels and title
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Performance')
    ax.set_title('Performance Trend of Teams')
    ax.legend()
    
    # Return the performance data and the figure object
    return performance_data, fig