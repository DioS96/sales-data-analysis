import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 

def remove_duplicates(dataframe):
    dupl_rows=dataframe.duplicated().sum()
    dataframe=dataframe.drop_duplicates()
    print(f"{dupl_rows} duplicates have been found and removed from the dataframe.")
    return dataframe

def cast_columns(dataframe, columns_dict={}, date_format="%Y-%m-%d"):

    for column, dtype in columns_dict.items():

        if dtype == "str":
            dataframe[column] = dataframe[column].astype("string")

        elif dtype == "int":
            dataframe[column] = dataframe[column].astype("Int64")

        elif dtype == "float":
            dataframe[column] = dataframe[column].astype("float")

        elif dtype == "date":
            dataframe[column] = pd.to_datetime(dataframe[column],format=date_format)

    return dataframe


def inconsistent_values(dataframe, min_num_value=0):

    # Creates 2 lists. One for numeric columns and one for the date columns.
    # Loops in num list, removes from the dataframe numeric values with <=0 and saves them in a separate dataframe.
    # Loops in date list, removes from the dataframe date greater than the current date and saves in a separate dataframe.

    inc_values_df = pd.DataFrame()

    num_cols = dataframe.select_dtypes(include=["number"]).columns

    date_cols = dataframe.select_dtypes(include=["datetime64"]).columns

    for col in num_cols:
        num_inc_rows = dataframe[dataframe[col] <= min_num_value]

        inc_values_df = pd.concat([inc_values_df, num_inc_rows])
        dataframe = dataframe[dataframe[col] > min_num_value]

        print(f"The {col} contains {len(num_inc_rows)} incosistent numbers which have been excluded from the analysis.")
        print(f"Adding these values to the incosistent_values_df")

    for col in date_cols:
        date_inc_rows = dataframe[dataframe[col] > pd.Timestamp("today")]

        inc_values_df = pd.concat([inc_values_df, date_inc_rows])
        dataframe = dataframe[dataframe[col] <= pd.Timestamp("today")]

        print(f"The {col} contains {len(date_inc_rows)} incosistent dates which have been excluded from the analysis.")
        print(f"Adding these values to the incosistent_values_df")

    return dataframe, inc_values_df



def replace_string_values(dataframe,column,replace_parameteres):

    #Cleans the incosistent values of the column with the use of the replace pd function. Returns the dataframe cleaned.
    #Parse parameters the dataframe, the column and the replace_parameteres dictionary to clean the str values.

    # Removes any possible spaces and trims the column's values.
    dataframe[column]=dataframe[column].str.strip()

    # Converts the string to upper letters if it equal or less than 3 digit.Otherwise converts to upper only the first letter.
    dataframe[column]=dataframe[column].apply(lambda x: x.upper() if len(x)<=3 else x.title())

    dataframe[column]=dataframe[column].replace(replace_parameteres)
    return dataframe

def find_max_value(dataframe,column):
    max_value=dataframe[column].max()
    return max_value

def find_min_value(dataframe,column):
    min_value=dataframe[column].min()
    return min_value

def find_average_value(dataframe,column):
    mean_value=dataframe[column].mean()
    return mean_value

def find_sum_value(dataframe,column):
    sum_value=dataframe[column].sum()
    return sum_value


def group_by(dataframe,groupby_columns,group_by_parameters):
    #Group by function under the column list in parameteres and the agg pandas function with group_by_parameteres in a dictionary format.

    summary_df=dataframe.groupby(groupby_columns).agg(group_by_parameters)
    return summary_df

def create_basic_analysis_table(dataframe,revenue_col,orders_col,category_col, payment_col,country_col,place="country",method="payment"):

    analysis_table=pd.DataFrame(
        {
            "Total_revenue": [dataframe[revenue_col].sum()],
            "Total_orders":[dataframe[orders_col].count()],
            "Average_order_value": [dataframe[revenue_col].mean()],
            "Top Category":[dataframe.groupby(category_col)[revenue_col].sum().idxmax()],
            f"Most Common {method}":[dataframe.groupby(payment_col)[orders_col].count().idxmax()],
            f"Most Profitable {place} in Total Values":[dataframe.groupby(country_col)[revenue_col].sum().idxmax()],
           f"Least Profitable {place} in Total Values":[dataframe.groupby(country_col)[revenue_col].sum().idxmin()]
        }
    )

    return analysis_table


def create_bar_chart(dataframe,x_column,y_column, estimator,chart_title,x_title,y_title,filter=None, palette="viridis"):

    # Sort dataframe in descending order
    sorted_df=dataframe.sort_values(
        by=y_column,
        ascending=False
        )

    # Formating the graph's size 
    plt.figure(figsize=(10,10))

    # Create simple bar chart
    barchart= sns.barplot(
                x=x_column ,
                y=y_column, 
                data=sorted_df,
                errorbar=None,
                estimator=estimator,
                hue=filter,
                palette=palette)
    
    # Chart title
    plt.title(chart_title,fontsize=20)

    # Axis titles
    plt.xlabel(x_title,fontsize=15)
    plt.ylabel(y_title,fontsize=15)
    
    # Legend position
    plt.legend(loc="upper right")

    plt.show()

    return barchart

def create_lineplot_graph(dataframe,x_column,y_column,estimator,chart_title,x_title,y_title,filter=None, palette="deep"):

    # Formating the graph's size 
    plt.figure(figsize=(10,10))
    
    # Create a line plot 

    lineplot=sns.lineplot(
        data=dataframe,
        x=x_column,
        y=y_column,
        estimator=estimator,
        errorbar=None,
        hue=filter,
        palette=palette
    )

    #Chart title
    plt.title(chart_title, fontsize=20)

    # Axis titles
    plt.xlabel(x_title,fontsize=15)
    plt.ylabel(y_title,fontsize=15)

    #Positioning the legend
    plt.legend(loc="upper right")

    plt.show()

    return lineplot

def create_scatterplot(dataframe,x_column,y_column,chart_title,x_title,y_title,filter=None, palette="muted"):

    # Formating the graph's size 
    plt.figure(figsize=(10,10))

    #Create a scatterplot graph

    scatterplot=sns.scatterplot(
        data=dataframe,
        x=x_column,
        y=y_column,
        hue=filter,
        palette=palette,
        alpha=0.7
    )
    
    # Adding graph title
    plt.title(chart_title,fontsize=20)

    # Adding axis titles
    plt.xlabel(x_title,fontsize=15)
    plt.ylabel(y_title,fontsize=15)

    plt.show()

    return scatterplot

def create_histogram(dataframe,column,filter=None,palette="viridis"):

    # Formating the graph's size 
    plt.figure(figsize=(10,10))

    # Create histogram
    histogram=sns.histplot(
        dataframe[column], 
        kde=True,
        hue=filter,
        color=sns.color_palette(palette)[3]
    )

    # Adding graph title
    plt.title(f"{column.title()} Distribution")

    # Adding axis titles
    plt.xlabel(column.title(),fontsize=15)
    plt.ylabel("Count",fontsize=15)

    plt.show()

    return histogram

def create_heatmap(dataframe,numeric_cols=[],palette="coolwarm"):

    # Formating the graph's size 
    plt.figure(figsize=(10,10))

    # Creating coorelation matrix
    matrix=dataframe[numeric_cols].corr()

    # Creating heatmap
    heatmap=sns.heatmap(
        matrix,
        annot=True,
        cmap=palette
    )

    # Adding title
    plt.title("Coorelation Heatmap")

    plt.show()

    return matrix

