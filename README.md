# sales-data-analysis
Exploratory data analysis project using Python, Pandas and Seaborn
# Data Analysis Project

## Overview

This project performs data analysis on a transactional sales dataset using Python. The workflow includes:

* Data loading and preprocessing
* Automated analysis functions
* Data cleaning and validation
* Exploratory data analysis (EDA)
* Aggregation calculations
* Data visualization

The analysis was developed in a Jupyter Notebook environment.

## Technologies Used

* Python
* Jupyter Notebook
* Pandas
* Matplotlib
* Seaborn


## Project Structure

project-folder/
│
├── main.ipynb
├── dataset.csv
├── README.md


## Features Implemented

### Data Cleaning

* Removed duplicate rows
* Parsed and corrected datatypes
* Handled missing values
* Detected inconsistent values

Missing and inconsistent values have been removed from the analysis and stored separately for subsequent investigation or reporting. The cleansing process is based on the implemented cleaning and inconsistency‑detection function, and the analyst may modify its parameters when applying it to other datasets.

### Data Analysis

* Revenue calculation
* GroupBy analysis
* Summary statistics
* Aggregations by categories and payment methods

The automated analysis functions are designed to help analysts explore extensive operational aggregations and derive meaningful insights by adjusting parameters like columns, aggregation methods, and more.

### Data Visualization

* Charts and plots using Matplotlib and Seaborn
* Visualization of sales trends and distributions

Data visualization functions have also been developed. Each function generates a single graph, and the analyst can apply them to different dataframes and parameters to produce a wide range of insights for both categorical and numerical data, supporting the investigation of potential correlations.

## Dataset

The dataset contains transactional sales information such as:

* Order ID
* Customer ID
* Product Name
* Category
* Quantity
* Unit Price
* Order Date
* Payment Method
* Country

## Author

Created by DioS96
