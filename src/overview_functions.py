import pandas as pd


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

