
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

# Load the data
df = pd.read_csv('data.csv')

# Perform feature selection with SelectKBest
selector = SelectKBest(k=2)
selector.fit(df, df['target'])

# Get the selected features
selected_features = selector.get_support(indices=True)

# Create a heatmap of the feature correlations
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Print the selected features
print(selected_features)