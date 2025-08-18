from scipy.stats import mannwhitneyu


def multiple_results_mwu(data_negative, data_positive, column: str):
    """
    Perform a Mann-Whitney U test between two groups for a specified column.

    Parameters
    ----------
    data_negative : pandas.DataFrame
        Dataset containing the first group of values.
    data_positive : pandas.DataFrame
        Dataset containing the second group of values.
    column : str
        The column name on which to perform the test.

    Prints
    ------
    str
        The U statistic and p-value for the Mann-Whitney U test.
        A message indicating whether the difference between groups
        is statistically significant (p <= 0.05).
    """
    stat, p = mannwhitneyu(data_negative[column], data_positive[column])
    print(f'{column}: U={stat:.3f}, p={p:.3f}')

    if p <= 0.05:
        print("Result: Statistically significant difference between groups.")
    else:
        print("Result: No significant difference between groups.")

    return stat, p
