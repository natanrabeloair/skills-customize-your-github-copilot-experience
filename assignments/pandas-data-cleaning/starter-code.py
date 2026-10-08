# Starter code for the pandas data-cleaning assignment

import pandas as pd


def load_data(file_path):
    """Load the student data from a CSV file."""
    pass


def clean_data(data):
    """Remove duplicates and fix invalid or missing values."""
    pass


def summarize_data(data):
    """Group the cleaned data by city and calculate average scores."""
    pass


def main():
    dataset = load_data("data.csv")
    cleaned_data = clean_data(dataset)
    summary = summarize_data(cleaned_data)

    print("Cleaned data:")
    print(cleaned_data)
    print("\nAverage score by city:")
    print(summary)

    cleaned_data.to_csv("cleaned_students.csv", index=False)


if __name__ == "__main__":
    main()
