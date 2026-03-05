
import pandas as pd
import random
import csv

def task_func(n, 
           categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
           news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
           likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
           file_path='news_survey_data.csv',
           random_seed=None):
    # Generate random survey data
    data = []
    for i in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1
        data.append([site, category, response, value])
    
    # Write data to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    
    # Read data from CSV file and create DataFrame
    df = pd.read_csv(file_path)
    return df