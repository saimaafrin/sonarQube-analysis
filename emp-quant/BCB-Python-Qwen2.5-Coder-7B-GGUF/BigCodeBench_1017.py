
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Check if the target_column exists in the DataFrame
        if target_column not in df.columns:
            raise ValueError(f"The specified target_column '{target_column}' is not found in the CSV file.")
        
        # Separate the features and the target variable
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        
        # Initialize and train the Random Forest classifier
        rf_classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
        rf_classifier.fit(X_train, y_train)
        
        # Make predictions on the test set
        y_pred = rf_classifier.predict(X_test)
        
        # Generate the classification report
        report = classification_report(y_test, y_pred)
        
        return report
    
    except Exception as e:
        return str(e)