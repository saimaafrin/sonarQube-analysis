
import pandas as pd
import codecs

def decode_unicode_escapes(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Decodes all Unicode escape strings in the "UnicodeString" column of a given Pandas DataFrame.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The Pandas DataFrame containing the "UnicodeString" column.

    Returns
    -------
    pd.DataFrame
        The DataFrame with decoded strings in the "UnicodeString" column.

    Raises
    ------
    KeyError
        If the column "UnicodeString" does not exist in the DataFrame.
    TypeError
        If the input is not a Pandas DataFrame.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")
    if "UnicodeString" not in dataframe.columns:
        raise KeyError("Column 'UnicodeString' does not exist in the DataFrame.")

    # Decode the Unicode escape sequences in the "UnicodeString" column
    dataframe["UnicodeString"] = dataframe["UnicodeString"].apply(codecs.decode)

    return dataframe