"""
Visualizer Module

This module provides functionality for creating data visualizations for the Starbucks Global Store Data Analysis Program.

The Visualizer class contains static methods for generating various plots using matplotlib and seaborn,
including bar plots for top countries, cities, and Chinese cities with the most Starbucks stores.

Classes:
    Visualizer: A class containing static methods for data visualization.

Dependencies:
    matplotlib.pyplot: For creating plots.
    seaborn: For enhanced plot styling.
    typing: For type hinting.
    pandas: For data manipulation and analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class Visualizer:
    """
    A class for creating data visualizations.

    This class provides static methods to generate various plots for analyzing Starbucks store data,
    including bar plots for top countries, cities, and Chinese cities with the most stores.

    Methods:
        plot_top_n(data: pd.Series, n: int, title: str, xlabel: str, ylabel: str, horizontal: bool = False) -> None:
            Create a bar plot of the top n items in a series.
        plot_top_countries(df: pd.DataFrame, n: int = 10) -> None:
            Create a bar plot of the top n countries with the most Starbucks stores.
        plot_top_cities(df: pd.DataFrame, n: int = 10) -> None:
            Create a bar plot of the top n cities with the most Starbucks stores.
        plot_top_cn_cities(df: pd.DataFrame, n: int = 10) -> None:
            Create a horizontal bar plot of the top n Chinese cities with the most Starbucks stores.
    """

    @staticmethod
    def plot_top_n(data: pd.Series, n: int, title: str, xlabel: str, ylabel: str, horizontal: bool = False) -> None:
        """
        Create a bar plot of the top n items in a series.

        Args:
            data (pd.Series): The data series to plot.
            n (int): The number of top items to include in the plot.
            title (str): The title of the plot.
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            horizontal (bool, optional): Whether to create a horizontal bar plot. Defaults to False.
        """
        plt.figure(figsize=(12, 6))
        if horizontal:
            sns.barplot(y=data.index[:n], x=data.values[:n])
        else:
            sns.barplot(x=data.index[:n], y=data.values[:n])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45 if not horizontal else 0)
        plt.show()

    @classmethod
    def plot_top_countries(cls, df: pd.DataFrame, n: int = 10) -> None:
        """
        Create a bar plot of the top n countries with the most Starbucks stores.

        Args:
            df (pd.DataFrame): The DataFrame containing the Starbucks store data.
            n (int, optional): The number of top countries to include. Defaults to 10.
        """
        top_countries = df['Country'].value_counts().nlargest(n)
        cls.plot_top_n(top_countries, n, f'店铺数量排名前{n}的国家', '国家', '店铺数量')

    @classmethod
    def plot_top_cities(cls, df: pd.DataFrame, n: int = 10) -> None:
        """
        Create a bar plot of the top n cities with the most Starbucks stores.

        Args:
            df (pd.DataFrame): The DataFrame containing the Starbucks store data.
            n (int, optional): The number of top cities to include. Defaults to 10.
        """
        top_cities = df['City'].value_counts().nlargest(n)
        cls.plot_top_n(top_cities, n, f'店铺数量排名前{n}的城市', '城市', '店铺数量')

    @classmethod
    def plot_top_cn_cities(cls, df: pd.DataFrame, n: int = 10) -> None:
        """
        Create a horizontal bar plot of the top n Chinese cities with the most Starbucks stores.

        Args:
            df (pd.DataFrame): The DataFrame containing the Starbucks store data for China.
            n (int, optional): The number of top cities to include. Defaults to 10.
        """
        top_cn_cities = df['City'].value_counts().nlargest(n)
        cls.plot_top_n(top_cn_cities, n, f'中国星巴克店铺数量前{n}的城市', '店铺数量', '城市', horizontal=True)
