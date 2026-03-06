import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results. This function is
    useful for preprocessing data for machine learning models where data scaling can impact performance.

    Parameters:
    data_dict (dict): A dictionary where keys map to lists of numeric values.
    data_keys (list): Keys within the dictionary whose corresponding values are to be normalized.

    Returns:
    tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the
    normalized data.

    Requirements:
    - pandas
    - sklearn

    Raises:
    ValueError: If no keys in `data_keys` are found in `data_dict`.

    Example:
    >>> data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    >>> data_keys = ['A', 'B']
    >>> normalized_df, ax = task_func(data_dict, data_keys)
    >>> print(normalized_df.to_string(index=False))
      A   B
    0.0 0.0
    0.5 0.5
    1.0 1.0
    """
    if not isinstance(data_dict, dict):
        raise ValueError('data_dict must be a dictionary.')
    if not isinstance(data_keys, list):
        raise ValueError('data_keys must be a list.')

    # Check that all keys in data_keys are in data_dict
    for key in data_keys:
        if key not in data_dict:
            raise ValueError('Key {} not found in data_dict.'.format(key))

    # Create a DataFrame of normalized values
    normalized_df = pd.DataFrame()
    for key in data_keys:
        normalized_df[key] = MinMaxScaler().fit_transform(data_dict[key])

    # Plot the normalized values
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    normalized_df.plot(ax=ax)
    ax.set_title('Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xticks(range(len(normalized_df)))
    ax.set_xticklabels(normalized_df.index)
    ax.set_yticks(range(0, 1, 0.1))
    ax.set_yticklabels(ax.get_yticks())
    ax.grid(True)

    return normalized_df, ax