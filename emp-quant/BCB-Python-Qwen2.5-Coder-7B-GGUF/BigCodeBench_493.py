
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
    end_date = datetime.now()
    delta = end_date - start_date
    days = [start_date + timedelta(days=i) for i in range(delta.days + 1)]
    
    # Initialize performance data dictionary
    performance_data = {team: [] for team in teams}
    
    # Set random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random performance data for each team
    for day in days:
        for team in teams:
            performance_data[team].append(random.uniform(0.1, 1))
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot performance data for each team
    for team, performance in performance_data.items():
        ax.plot(days, performance, label=team)
    
    # Set labels and title
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Performance')
    ax.set_title('Performance Trend of Teams')
    ax.legend()
    
    return performance_data, fig