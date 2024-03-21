"""
This is a script primarily designed to help during the data cleaning process. 
The functions created in this .py file will focus on:
    1. Handling Null Values - Dropping or Aggregating
    2. Remove duplicates observations
    3. Convert Data types for future analysis - Numerical - DateTime
"""
# Packages
import pandas as pd


# Function 1 - Standardize Text - lower case/upper case
def standardize_text_casing(df):
    string_columns = df.select_dtypes(include=['object', 'string']).columns # selects columns that have data types suitable for string operations
    for column_name in string_columns:
        df[column_name] = df[column_name].str.lower().strip()#strip from both sides
    return df

# Function 2 - Convert Data Types - This requires initial inspection of datatypes in df
def convert_datatypes(df,dtypes_in_columns):
    for column, dtype in dtypes_in_columns.items():
        if column in df.columns:
            df[column] = df[column].astype(dtype)
        else:
            print(f"The column name {column} does not exist in the dataset. Please Revise")
    return df

# Function 3 - Remove Null Values
def remove_null_values(df, threshold=0.5): # This set parameter can be changed based on the requirements
    null_percentage = df.isnull().mean()
    columns_to_drop = null_percentage[null_percentage > threshold].index
    df_cleaned = df.drop(columns = columns_to_drop)
    return df_cleaned

# Function 4 - Replace Null Values with average value of the column
def replace_null_with_mean(df,column_name): # Ensure Pandas is uploaded
    if column_name in df.columns:
        mean_value = df[column_name].mean()
        df[column_name].fillna(mean_value, inplace = True)
    else:
        print(f'The Column Name, {column_name} does not exist in your dataset. Please revise')
    return df

# Function 5 - Replace null Values with median value of a column 
def replace_null_with_median(df,column_name): # Ensure Pandas is uploaded
    if column_name in df.columns:
        median_value = df[column_name].median()
        df[column_name].fillna(median_value, inplace = True)
    else:
        print(f'The Column Name, {column_name} does not exist in your dataset. Please revise')
    return df