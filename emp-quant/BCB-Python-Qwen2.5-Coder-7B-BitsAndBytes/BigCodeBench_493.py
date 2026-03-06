
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
    today = datetime.today()
    delta = today - start_date
    num_days = delta.days + 1
    
    # Initialize performance data dictionary
    performance_data = {team: [] for team in teams}
    
    # Set random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random performance data for each team
    for _ in range(num_days):
        for team in teams:
            performance_data[team].append(round(random.uniform(0.1, 1), 2))
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot performance data for each team
    for team, perf in performance_data.items():
        ax.plot(range(num_days), perf, label=team)
    
    # Set labels and title
    ax.set_xlabel('Days Since Start Date')
    ax.set_ylabel('Performance')
    ax.set_title('Performance Trend Over Time')
    ax.legend()
    
    return performance_data, fig