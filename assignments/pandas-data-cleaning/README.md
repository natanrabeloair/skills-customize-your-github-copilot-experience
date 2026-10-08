# 📘 Assignment: Data Cleaning with pandas

## 🎯 Objective

Use Python and the pandas library to clean a student performance dataset. You will load the data, remove duplicate and invalid records, and create a summary that reveals useful statistics.

## 📝 Tasks

### 🛠️ Load and Inspect the Dataset

#### Description
Load the provided CSV file with pandas and inspect its columns, rows, and data types.

#### Requirements
Completed program should:

- Import pandas as `pd`.
- Load the dataset using `pd.read_csv()`.
- Print the number of rows and columns.
- Display the first five rows.
- Display the data types for each column.

### 🛠️ Clean the Data

#### Description
Remove duplicate records and correct incomplete or invalid values in the dataset.

#### Requirements
Completed program should:

- Remove duplicate rows using `drop_duplicates()`.
- Convert the `age` column to numeric values using `pd.to_numeric()`.
- Replace missing values in the `score` column with the column mean.
- Remove rows where `age` is missing or invalid.
- Print the cleaned dataset before creating the summary.

### 🛠️ Create a Summary

#### Description
Create a concise summary of the cleaned student data.

#### Requirements
Completed program should:

- Group the cleaned data by `city`.
- Calculate the average score for each city.
- Sort the results from highest to lowest average score.
- Print the summary table.
- Save the cleaned data to a new CSV file named `cleaned_students.csv`.

The starter code includes the required function structure. Use the provided dataset as the source file and run the program from this assignment folder.
