import pandas as pd

file = input("Enter CVS file path:")
data=pd.read_csv(file)

print("\n Data Preview:\n", data)