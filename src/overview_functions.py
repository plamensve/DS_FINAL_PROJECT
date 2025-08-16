import numpy as np
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


def display_scatterplot_by_features(dataset, *args):
    """
    Display scatterplot of selected features against the binary target.

    Each feature in *args is plotted on the Y-axis, while the target variable 'heart_disease'
    (0 = Negative, 1 = Positive) is plotted on the X-axis with added jitter to improve visibility.
    Points are colored according to the target value.

    Parameters
    ----------
    dataset : pandas.DataFrame
        The dataset containing the features and the target column 'heart_disease'.
    *args : str
        One or more feature names (columns) to visualize against the target.

    Returns
    -------
    None
        Displays the scatterplots directly using matplotlib.
    """
    features = args

    for f in features:
        plt.figure(figsize=(8, 6))

        x = dataset["heart_disease"] + np.random.normal(0, 0.02, size=len(dataset))

        y = dataset[f]

        plt.scatter(x, y, alpha=0.6, c=dataset["heart_disease"], cmap="coolwarm")
        plt.xticks([0, 1], ["Negative", "Positive"])
        plt.xlabel("Heart Disease")
        plt.ylabel(f.capitalize())
        plt.title(f"{f.capitalize()} by Heart Disease")
        plt.show()
    """
       Explanation of the scatterplot code:

       - Loop over selected features: We iterate through the key features (`age`, `kcm`, `troponin`) 
         to create a separate scatterplot for each.  
       - Jitter on the X-axis:
         x = dataset1["heart_disease"] + np.random.normal(0, 0.02, size=len(dataset1))  
         Since 'heart_disease' only takes values 0 or 1, all points would align in two vertical lines. 
         Adding a small random noise ("jitter") spreads the points slightly, making the distribution clearer.  
       - Scatterplot:
         plt.scatter(x, y, alpha=0.6, c=dataset1["heart_disease"], cmap="coolwarm")  
           - alpha=0.6: makes points semi-transparent to reduce overlap.  
           - c=dataset1["heart_disease"]: colors the points based on the target variable (0 = Negative, 1 = Positive).  
           - cmap="coolwarm": provides a contrasting color scheme (e.g., blue vs. red).  
       - Axis labels and ticks:  
           - plt.xticks([0,1], ["Negative","Positive"]): replaces numeric labels with more descriptive ones.  
           - plt.xlabel, plt.ylabel, plt.title: add informative labels and a title for each plot.  
    """
