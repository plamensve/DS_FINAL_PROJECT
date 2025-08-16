import unittest
import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from src.overview_functions import display_scatterplot_by_features


class TestVisualizationFunctions(unittest.TestCase):

    def setUp(self):
        plt.show = lambda *args, **kwargs: None

        self.df = pd.DataFrame({
            "age": [20, 30, 40, 50, 60],
            "kcm": [1.1, 2.2, 3.3, 4.4, 5.5],
            "troponin": [0.01, 0.02, 0.05, 0.10, 0.20],
            "heart_disease": [0, 1, 0, 1, 1],
        })

    def test_display_scatterplot_by_features_runs(self):
        """Check if scatterplot runs without error."""
        try:
            display_scatterplot_by_features(self.df, "age", "kcm")
        except Exception as e:
            self.fail(f"display_scatterplot_by_features raised an exception: {e}")

    def test_display_scatterplot_by_features_invalid_column(self):
        """Check if invalid feature raises KeyError."""
        with self.assertRaises(KeyError):
            display_scatterplot_by_features(self.df, "not_a_col")


if __name__ == '__main__':
    unittest.main()
