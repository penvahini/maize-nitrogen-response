# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:41:29 2024

@author: cjinr
"""

import pandas as pd

# Load the Excel file
df = pd.read_excel("C:path/to/GO_enrichment.xlsx", engine='openpyxl')

# Display the first few rows
print("First few rows:")
print(df.head())

# Summary of the dataframe
print("\nDataFrame Info:")
print(df.info())

# Statistical summary for numeric columns
print("\nStatistical Summary:")
print(df.describe())

# Number of rows and columns
print("\nDataFrame Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())


modules_of_interest = [1, 6, 10, 12, 13, 15, 17, 19]

# Filter to only include rows where 'module' is in the list of interest
filtered_df = df[df['module'].isin(modules_of_interest)]

# Display filtered DataFrame
print(filtered_df)

# Save filtered data to new excel file
filtered_df.to_excel("filtered_data.xlsx", index=False)


df_scored = pd.read_excel("C:\\Users\\cjinr\\OneDrive\\Documents\\Grad School Documents\\BICB\\CSCI5461\\Project\\filtered_data.xlsx", engine='openpyxl')

#Group by 'module', then apply nlargest to get the top 4 for '% Overlap' within each group
top_overlap_per_module = df_scored.groupby('module').apply(lambda x: x.nlargest(4, '% Overlap')).reset_index(drop=True)

# Display result
print(top_overlap_per_module)

#Save to new excel file
top_overlap_per_module.to_excel("Top_4_per_module.xlsx", index=False)


