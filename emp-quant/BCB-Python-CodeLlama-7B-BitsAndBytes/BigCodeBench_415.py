
import pandas as pd
import codecs

def task_func(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Decodes all Unicode escape strings in a particular column ("UnicodeString") in a given Pandas DataFrame.

    Args:
        dataframe (pd.DataFrame): The Pandas DataFrame to decode.

    Returns:
        pd.DataFrame: The DataFrame with decoded strings in the "UnicodeString" column.

    Raises:
        KeyError: If the column "UnicodeString" does not exist in the DataFrame.
        TypeError: If the input is not a Pandas DataFrame.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")
    if "UnicodeString" not in dataframe.columns:
        raise KeyError("Column 'UnicodeString' does not exist in the DataFrame.")

    # Create a new column to store the decoded strings
    decoded_dataframe = dataframe.copy()
    decoded_dataframe["DecodedString"] = decoded_dataframe["UnicodeString"].apply(lambda x: codecs.decode(x, "unicode_escape"))

    return decoded_dataframe