"""
Analyzer Module

This module provides functionality for analyzing data in the Starbucks Global Store Data Analysis Program.

The Analyzer class contains methods for performing various analyses on the Starbucks store data,
including calculating total stores, unique countries, and identifying top countries and cities.

Classes:
    Analyzer: A class containing methods for data analysis and result formatting.

Dependencies:
    pandas: For data manipulation and analysis.
    typing: For type hinting.
"""

import pandas as pd
from typing import Dict, Any

class Analyzer:
    """
    A class for analyzing Starbucks store data.

    This class provides methods to perform various analyses on the Starbucks store data
    and format the results for presentation.

    Methods:
        analyze_data(df: pd.DataFrame) -> Dict[str, Any]:
            Perform analysis on the given DataFrame and return the results.
        format_analysis(analysis: Dict[str, Any]) -> str:
            Format the analysis results into a human-readable string.
    """

    @staticmethod
    def analyze_data(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Perform analysis on the given DataFrame.

        This method calculates various statistics from the Starbucks store data,
        including total number of stores, number of countries, top country, and top city.

        Args:
            df (pd.DataFrame): The DataFrame containing the Starbucks store data.

        Returns:
            Dict[str, Any]: A dictionary containing the analysis results.
                Keys include:
                - 'total_stores': Total number of unique stores
                - 'total_countries': Total number of unique countries
                - 'top_country': Country with the most stores
                - 'top_city': City with the most stores
        """
        return {
            'total_stores': df['Store Number'].nunique(),
            'total_countries': df['Country'].nunique(),
            'top_country': df['Country'].value_counts().index[0],
            'top_city': df['City'].value_counts().index[0]
        }

    @staticmethod
    def format_analysis(analysis: Dict[str, Any]) -> str:
        return (f"星巴克在全球共有 {analysis['total_stores']} 家店铺，"
                f"分布在 {analysis['total_countries']} 个国家和地区，"
                f"店铺数量最多的国家是 {analysis['top_country']}，"
                f"城市是 {analysis['top_city']}。")
