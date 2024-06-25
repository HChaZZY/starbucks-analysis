"""
Starbucks Analysis Program

HangZhou Dianzi University 2023-2024 Semester Final Project

This module serves as the main entry point for the program, coordinating the work of various components
including data processing, visualization, and analysis.

Main functionalities:
1. Read and process Starbucks global store data
2. Perform data cleaning and transformation
3. Generate data visualization charts
4. Conduct data analysis and output results

Dependencies:
- data_processor: For data processing tasks
- visualizer: For data visualization
- analyzer: For data analysis
- config_manager: For managing configuration information
"""

from data_processor import DataProcessor, fill_city
from visualizer import Visualizer
from analyzer import Analyzer
from config_manager import ConfigManager

def main():
    """
    Main function that coordinates the execution flow of the entire program.

    Key steps:
    1. Initialize the configuration manager
    2. Read and process data
    3. Display data statistics
    4. Perform data cleaning and transformation
    5. Save the processed data
    6. Generate visualization charts
    7. Process Starbucks data for China
    8. Conduct data analysis and output results

    No parameters, no return value
    """

    config = ConfigManager()

    processor = DataProcessor(config.get('input_file'))
    print("前五行数据：")
    print(processor.head)

    print("\n缺失值情况：")
    print(processor.missing_data)

    print("\nCity字段缺失的数据：")
    print(processor.city_null)

    processor.apply_function(fill_city, 'City')

    print("\n填充后的埃及(EG)数据：")
    print(processor.filter_by_country('EG'))

    unique_brands = processor.df['Brand'].unique()
    print("\n唯一的Brand值：", unique_brands)

    processor.replace_values('Brand', dict.fromkeys(unique_brands, 'Starbucks'))

    processor.save_to_csv(config.get('output_file'))
    print(f"\n数据已保存到{config.get('output_file')}")

    Visualizer.plot_top_countries(processor.df)
    Visualizer.plot_top_cities(processor.df)

    cn_starbucks = processor.filter_by_country('CN')
    print("\n中国星巴克分布（前五行）：")
    print(cn_starbucks.head())

    cn_starbucks.to_csv(config.get('cn_output_file'), index=False)
    print(f"\n中国星巴克数据已保存到{config.get('cn_output_file')}")

    Visualizer.plot_top_cn_cities(cn_starbucks)

    analyzer = Analyzer()
    analysis = analyzer.analyze_data(processor.df)
    print(analyzer.format_analysis(analysis))

if __name__ == "__main__":
    main()
