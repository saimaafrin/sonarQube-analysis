import pandas as pd
import random
import csv
def task_func(n, 
           categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
           news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
           likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
           file_path='news_survey_data.csv',
           random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Create a list to store the survey data
    data = []
    
    # Generate random survey data
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1  # Assign numerical value starting from 1
        data.append([site, category, response, value])
    
    # Create a DataFrame from the survey data
    df = pd.DataFrame(data, columns=['Site', 'Category', 'Response', 'Value'])
    
    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Read the CSV file back into a DataFrame
    df = pd.read_csv(file_path)
    
    return df