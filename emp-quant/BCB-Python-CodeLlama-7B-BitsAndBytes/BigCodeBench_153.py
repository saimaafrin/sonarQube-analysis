
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    # Create a new DataFrame with columns 'Category' and 'Encoded'
    encoded_data = pd.DataFrame(columns=['Category', 'Encoded'])

    # Initialize a LabelEncoder object
    le = LabelEncoder()

    # Encode each category in the data
    for category in data['Category']:
        # Encode the category using the LabelEncoder
        encoded_category = le.fit_transform(category)

        # Add the encoded category to the DataFrame
        encoded_data = encoded_data.append({'Category': category, 'Encoded': encoded_category}, ignore_index=True)

    # Return the encoded DataFrame
    return encoded_data