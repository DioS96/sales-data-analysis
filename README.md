# Sales-data-analysis
Exploratory data analysis project using Python, Pandas and Seaborn

## Overview

This project performs exploratory data analysis (EDA) on transactional sales datasets using Python. The analysis is based on both mock Excel/CSV data and dummy JSON data retrieved from the free DummyJSON API. The project includes automated workflows for data loading, preprocessing, cleansing, validation, aggregation, analysis, and visualization.

The workflow was developed in a Jupyter Notebook environment and is supported by reusable utility functions organized into service modules. In addition, the project includes unit testing with Pytest and CI/CD pipeline integration to support code quality and automation.

Key features include:

- Data loading and preprocessing
- Automated data analysis functions
- Data cleaning and validation
- Exploratory data analysis (EDA)
- Aggregation and summary calculations
- Data visualization
- API data extraction using DummyJSON
- Unit testing with Pytest
- CI/CD workflow integration

## Technologies Used

* Python
* Jupyter Notebook
* Pandas
* Matplotlib
* Seaborn
* Requests
* Pytest
* CI/CD


## Project Structure

```
sales-data-analysis/
│
├── services/                             # Core utility and API functions
│   ├── __init__.py
│   ├── api.py
│   └── functions.py
│
├── tests/                                # Unit tests
│   └── test_functions.py
│
├── dummy_json_analysis_visualization.ipynb   # Analysis & visualization of DummyJSON data
├── mock_data_analysis_visualization.ipynb    # Analysis & visualization of mock transactional data
├── mock_ecommerce_dataset_2000_rows.csv      # Mock e-commerce transactional dataset
├── README.md
└── requirements.txt                      # Project dependencies
```
## Installation - How to build
Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

Ensure Git is installed
Download and install Git if needed:
https://git-scm.com

Clone the repository
git clone https://github.com/DioS96/sales-data-analysis.git

Navigate to the project directory
cd sales-data-analysis

Check Python installation
python --version

Install project dependencies
pip install -r requirements.txt

Run tests
pytest

Launch Jupyter Notebook
jupyter notebook

Open one of the notebooks:
 - dummy_json_analysis_visualization.ipynb
 - mock_data_analysis_visualization.ipynb


## Services

This folder includes three Python files: `api.py`, `functions.py`, and `__init__.py`. The first two contain automated and reusable functions that are later used in the notebooks. The `__init__.py` file is included to support the testing setup.

### api.py

`api_get_data()` is a reusable function for retrieving data from the DummyJSON API with customizable endpoints and parameters, including basic error handling.

`convert_to_pandas_df()` transforms raw JSON API responses into structured Pandas DataFrames, supporting both simple and nested JSON normalization for data analysis workflows.

### funtions.py

`remove_duplicates()` identifies and removes duplicate rows from a DataFrame while reporting the number of duplicates removed.

`cast_columns()` converts DataFrame columns into specified data types, including strings, integers, floats, and datetime formats, to ensure data consistency.

`inconsistent_values()` detects and removes inconsistent numeric and date values, such as negative numbers or future dates, while storing excluded records in a separate DataFrame for further review.

`replace_string_values()` standardizes and cleans string-based column values by trimming spaces, formatting text casing, and replacing inconsistent values using a mapping dictionary.

`find_max_value()`, `find_min_value()`, `find_average_value()`, and `find_sum_value()` perform basic aggregation calculations on DataFrame columns.

`group_by()` applies grouped aggregations on selected columns using customizable aggregation parameters.

`create_basic_analysis_table()` generates a summary analysis table containing key business metrics such as total revenue, order count, average order value, top-performing categories, and profitability insights.

`create_bar_chart()`, `create_lineplot_graph()`, `create_scatterplot()`, `create_histogram()`, and `create_heatmap()` generate reusable data visualization charts using Matplotlib and Seaborn to support exploratory data analysis and trend identification.

## tests

This folder contains `test_functions.py`, which is used for unit testing and validation of the project's core functions.

### test_functions.py

test_functions.py contains unit tests for validating the project's reusable data processing and analysis functions. The tests verify functionality related to data cleaning, duplicate removal, datatype casting, inconsistent value handling, string replacement operations, and aggregation calculations using the Pytest framework.

`test_replace_string_values()` validates that inconsistent string values are correctly standardized and replaced.

`test_max()` verifies that the maximum value calculation function returns the correct result.

`test_remove_duplicates()` checks whether duplicate rows are successfully removed from a DataFrame.

`test_cast_columns()` ensures that DataFrame columns are correctly converted to the specified data types.

`test_incosisten_values()` validates that inconsistent numeric and date values are properly identified and excluded from the dataset.

## dummy_json_analysis_visualization.ipynb

This notebook focuses on retrieving and analyzing e-commerce data from the DummyJSON API. The workflow includes API data extraction, JSON normalization, data cleansing, datatype validation, duplicate removal, and exploratory analysis of carts and products datasets. The notebook demonstrates how reusable automation functions can simplify API-driven data analysis workflows and prepare nested JSON data for visualization and reporting.

Key findings and focus areas:
- Transformation of nested API JSON responses into structured DataFrames
- Identification and removal of inconsistent or duplicate records
- Analysis of product and cart-related transactional patterns
- Demonstration of reusable ETL-style data preparation workflows


## mock_data_analysis_visualization.ipynb

This notebook performs exploratory data analysis on a mock e-commerce transactional dataset stored in CSV format. The workflow includes data cleansing, null handling, datatype conversion, inconsistent value detection, feature engineering, aggregation analysis, and data visualization using Matplotlib and Seaborn.

Key findings and focus areas:
- Cleaning and standardizing transactional sales data
- Revenue calculation and business metric generation
- Analysis of country, category, and payment trends
- Visualization of distributions, correlations, and sales patterns
- Demonstration of automated reusable analysis and visualization functions


### Data Visualization

* Charts and plots using Matplotlib and Seaborn
* Visualization of sales trends and distributions

Data visualization functions have also been developed. Each function generates a single graph, and the analyst can apply them to different dataframes and parameters to produce a wide range of insights for both categorical and numerical data, supporting the investigation of potential correlations.

## Additional info 

### mock_ecommerce_dataset_2000_rows.csv

This dataset contains mock e-commerce transactional sales data used for exploratory data analysis, data cleaning, aggregation calculations, and visualization tasks throughout the project. It simulates real-world business data such as orders, customers, revenue, payment methods, categories, and regional sales activity.


### requirements.txt

This file contains all Python package dependencies required to run the project successfully. It is used to automatically install the libraries needed for data processing, analysis, visualization, API requests, notebook execution, and testing.

## Author

Created by DioS96

