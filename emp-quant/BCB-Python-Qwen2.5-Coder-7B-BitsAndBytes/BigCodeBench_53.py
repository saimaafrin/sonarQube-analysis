
import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    # Define the regular expression pattern to extract data
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Create a list of dictionaries to store the extracted data
    data_list = []
    for match in matches:
        data_dict = {
            "Name": match[0],
            "Email": match[1],
            "Age": int(match[2]),  # Convert age to integer
            "Country": match[3]
        }
        data_list.append(data_dict)
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list, columns=COLUMN_NAMES)
    
    # Plot the age distribution using seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=range(10, 50, 5), kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    return df