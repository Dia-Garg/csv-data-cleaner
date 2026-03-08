import os
import pandas as pd

file = input("Enter CSV file name: ")

if not os.path.isfile(file):
    print("Invalid file path. Please enter a CSV file.")
else:
    data = pd.read_csv(file, sep=",", skipinitialspace=True)

    print("\nOriginal Data:")
    print(data)

    # Trim spaces from all text columns
    data = data.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    #Remove empty rows
    data = data.dropna(how="all")

    print("\nCleaned Data:")
    print(data)