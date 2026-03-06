
import pandas as pd
import random

def task_func(n, 
               categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
               news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
               likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
               file_path='news_survey_data.csv',
               random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Create a list of dictionaries to store the data
    data = []
    
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        
        # Map the response to a numerical value
        value = likert_scale.index(response) + 1
        
        data.append({'Site': site, 'Category': category, 'Response': response, 'Value': value})
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    
    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    return df