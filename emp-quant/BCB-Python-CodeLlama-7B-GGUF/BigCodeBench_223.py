
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df, dct, columns=None):
    """
    Preprocess a pandas DataFrame by replacing specified values, encoding categorical attributes, and standardizing numerical attributes.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be preprocessed.
    dct : dict
        A dictionary containing the preprocessing instructions.
    columns : list, optional
        A list of column names to be preprocessed. If None, all columns are preprocessed.

    Returns
    -------
    df : pandas.DataFrame
        The preprocessed DataFrame.

    Raises
    ------
    ValueError
        If the input df is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a pandas.DataFrame")

    # Replace specified values
    if "replace" in dct:
        for col, vals in dct["replace"].items():
            df[col] = df[col].replace(vals)

    # Encode categorical attributes
    if "encode" in dct:
        for col in dct["encode"]:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    # Standardize numerical attributes
    if "standardize" in dct:
        for col in dct["standardize"]:
            df[col] = (df[col] - df[col].mean()) / df[col].std()

    return df