import pandas as pd
from matplotlib import pyplot as plt


def convert_to_string_to_lower(dataset, column):
    """
    Convert the specified column in the given dataset to string type
    and transform all values to lowercase.

    Parameters:
        dataset (DataFrame): The DataFrame containing the column.
        column (str): The name of the column to be converted.

    Returns:
        Series: The transformed column with lowercase string values.
    """
    if not isinstance(dataset, pd.DataFrame):
        raise TypeError("dataset must be a pandas DataFrame")

    if not isinstance(column, str):
        raise TypeError("column name must be a string")

    if column not in dataset.columns:
        raise ValueError(f"Column '{column}' does not exist in the dataset.")

    dataset[column] = dataset[column].astype('string')
    dataset[column] = dataset[column].str.lower()
    return dataset[column]


def display_column_distribution(dataset, column_name):
    """
    Plot a histogram showing the distribution of a specific column.

    Parameters:
        dataset (DataFrame): The dataset containing the columns.
        column_name (str): Name of the numeric column to visualize.
    """
    ax = dataset[column_name].hist(figsize=(8, 6), edgecolor='black')
    ax.set_title(f'{column_name.capitalize()} Distribution')
    ax.set_xlabel(column_name.capitalize())
    ax.set_ylabel('Count')
    ax.grid(False)
    
    plt.show()