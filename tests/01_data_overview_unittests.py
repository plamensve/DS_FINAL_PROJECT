import unittest
import pandas as pd
from src.overview_functions import convert_to_string_to_lower


class TestConvertToStringToLower(unittest.TestCase):

    def test_lowercase_conversion(self):
        df = pd.DataFrame({'col': ['HELLO', 'World']})
        result = convert_to_string_to_lower(df, 'col')
        self.assertTrue(all(result == ['hello', 'world']))

    def test_numeric_values(self):
        df = pd.DataFrame({'col': [123, 456]})
        result = convert_to_string_to_lower(df, 'col')
        self.assertTrue(all(result == ['123', '456']))

    def test_mixed_values(self):
        df = pd.DataFrame({'col': ['HELLO', 123, None]})
        result = convert_to_string_to_lower(df, 'col')
        self.assertTrue(result.iloc[0] == 'hello')
        self.assertTrue(result.iloc[1] == '123')
        self.assertTrue(pd.isna(result.iloc[2]))

    def test_cyrillic(self):
        df = pd.DataFrame({'col': ['ТЕСТ', 'тЕсТ']})
        result = convert_to_string_to_lower(df, 'col')
        self.assertTrue(result.iloc[0] == 'тест')
        self.assertTrue(result.iloc[1] == 'тест')

    def test_dataset_not_dataframe(self):
        with self.assertRaises(TypeError) as context:
            convert_to_string_to_lower(["not", "a", "df"], "col")
        print("Raised message →", str(context.exception))
        self.assertIn("dataset must be a pandas DataFrame", str(context.exception))

    def test_column_not_string(self):
        df = pd.DataFrame({"col": ["Test"]})
        with self.assertRaises(TypeError) as context:
            convert_to_string_to_lower(df, 123)
        print("Raised message →", str(context.exception))
        self.assertIn("column name must be a string", str(context.exception))

    def test_column_not_in_dataframe(self):
        df = pd.DataFrame({"col": ["Test"]})
        with self.assertRaises(ValueError) as context:
            convert_to_string_to_lower(df, "missing_col")
        print("Raised message →", str(context.exception))
        self.assertIn("Column 'missing_col' does not exist", str(context.exception))


if __name__ == '__main__':
    unittest.main()
