
import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt
COLUMN_NAMES = ["Name", "Email", "Age", "Country"]
def task_func(text):
    # Extract data using regex
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Create DataFrame
    df = pd.DataFrame(matches, columns=COLUMN_NAMES)
    
    # Plot age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], kde=True, color='b', bins=30)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the DataFrame
    return df