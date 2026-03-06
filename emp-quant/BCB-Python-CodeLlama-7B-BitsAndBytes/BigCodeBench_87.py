
import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    # Set the random seed for reproducibility
    seed(random_seed)

    # Create a dictionary to store the ratings
    ratings_dict = {}

    # Loop through the products and generate ratings based on the weights
    for product in products:
        ratings_dict[product] = choices(ratings, weights=weights, k=1)[0]

    # Create a DataFrame from the ratings dictionary
    ratings_df = pd.DataFrame(ratings_dict, columns=['Product', 'Rating'])

    # Sort the DataFrame by rating in descending order
    ratings_df.sort_values(by='Rating', ascending=False, inplace=True)

    return ratings_df

# Generate the ratings DataFrame
ratings_df = task_func(products, ratings, weights)

# Print the results
print(ratings_df)