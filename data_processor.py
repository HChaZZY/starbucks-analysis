"""
Data Processor Module

This module provides functionality for processing and manipulating data for the Starbucks Global Store Data Analysis Program.

The DataProcessor class handles various data processing tasks such as reading CSV files, applying functions to columns,
replacing values, filtering data, and saving processed data.

Classes:
    DataProcessor: Manages data processing operations on a pandas DataFrame.

Functions:
    fill_city: A helper function to fill missing city values with state/province values.

Dependencies:
    pandas: For data manipulation and analysis.
    typing: For type hinting.
    functools: For partial function application.
    config_manager: For managing configuration settings.
"""

import pandas as pd
from typing import Callable, Any
from functools import partial
from config_manager import ConfigManager

class DataProcessor:
    """
    A class for processing and manipulating data stored in a pandas DataFrame.

    This class provides methods to read data from CSV files, apply functions to columns,
    replace values, filter data, and save processed data.

    Attributes:
        config (ConfigManager): An instance of ConfigManager for handling configuration settings.
        df (pd.DataFrame): The pandas DataFrame containing the data to be processed.

    Methods:
        __init__(self, file_path: str): Initialize the DataProcessor with data from a CSV file.
        apply_function(self, func: Callable[[pd.Series], Any], column: str) -> None: Apply a function to a specific column.
        replace_values(self, column: str, value_map: dict) -> None: Replace values in a column based on a mapping.
        filter_by_country(self, country_code: str) -> pd.DataFrame: Filter the DataFrame by country code.
        save_to_csv(self, file_path: str) -> None: Save the processed DataFrame to a CSV file.
        head(self) -> pd.DataFrame: Get the first few rows of the DataFrame.
        missing_data(self) -> pd.Series: Get information about missing data in the DataFrame.
        city_null(self) -> pd.DataFrame: Get rows where the 'City' column is null.
    """

    def __init__(self, file_path: str):
        """
        Initialize the DataProcessor with data from a CSV file.

        Args:
            file_path (str): The path to the CSV file to be processed.
        """
        self.config = ConfigManager()
        self.df = pd.read_csv(file_path)

    def apply_function(self, func: Callable[[pd.Series], Any], column: str) -> None:
        """
        Apply a function to a specific column in the DataFrame.

        Args:
            func (Callable[[pd.Series], Any]): The function to apply to the column.
            column (str): The name of the column to apply the function to.
        """
        self.df[column] = self.df.apply(func, axis=1)

    def replace_values(self, column: str, value_map: dict) -> None:
        """
        Replace values in a column based on a mapping.

        Args:
            column (str): The name of the column to replace values in.
            value_map (dict): A dictionary mapping old values to new values.
        """
        self.df[column] = self.df[column].replace(value_map)

    def filter_by_country(self, country_code: str) -> pd.DataFrame:
        """
        Filter the DataFrame by country code.

        Args:
            country_code (str): The country code to filter by.

        Returns:
            pd.DataFrame: A new DataFrame containing only rows for the specified country.
        """
        return self.df[self.df['Country'] == country_code]

    def save_to_csv(self, file_path: str) -> None:
        """
        Save the processed DataFrame to a CSV file.

        Args:
            file_path (str): The path where the CSV file should be saved.
        """
        self.df.to_csv(file_path, index=False)
        self.config.set('output_file', file_path)
        self.config.save()

    @property
    def head(self) -> pd.DataFrame:
        """
        Get the first few rows of the DataFrame.

        Returns:
            pd.DataFrame: The first few rows of the DataFrame.
        """
        return self.df.head()

    @property
    def missing_data(self) -> pd.Series:
        """
        Get information about missing data in the DataFrame.

        Returns:
            pd.Series: A series containing the count of missing values for each column with missing data.
        """
        return self.df.isnull().sum()[lambda x: x > 0]

    @property
    def city_null(self) -> pd.DataFrame:
        """
        Get rows where the 'City' column is null.

        Returns:
            pd.DataFrame: A DataFrame containing rows where the 'City' column is null.
        """
        return self.df[self.df['City'].isnull()]

def fill_city(row: pd.Series) -> str:
    """
    Fill missing city values with state/province values.

    Args:
        row (pd.Series): A row from the DataFrame.

    Returns:
        str: The city value if not null, otherwise the state/province value.
    """
    return row['State/Province'] if pd.isnull(row['City']) else row['City']
