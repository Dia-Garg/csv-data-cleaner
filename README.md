# CSV Data Cleaner

A Python automation tool that cleans messy CSV datasets.

This script loads a CSV file and prepares it for data processing by applying common cleaning operations.

## Features
- Remove empty rows
- Remove duplicate rows
- Trim extra spaces from cells
- Standardize column names
- Generate a cleaning report

## How It Works

The program asks the user for the CSV file path, loads the dataset using **pandas**, and performs cleaning operations automatically.

## Example

Messy data:

Name, Age , City  
Dia ,20 , Delhi  
Rahul, ,Mumbai  
Dia ,20 , Delhi  

Cleaned data:

name,age,city  
Dia,20,Delhi  
Rahul,,Mumbai  

## Technologies Used
- Python
- Pandas

## How to Run

Install dependencies:
# CSV Data Cleaner

A Python automation tool that cleans messy CSV datasets.

This script loads a CSV file and prepares it for data processing by applying common cleaning operations.

## Features
- Remove empty rows
- Remove duplicate rows
- Trim extra spaces from cells
- Standardize column names
- Generate a cleaning report

## How It Works

The program asks the user for the CSV file path, loads the dataset using **pandas**, and performs cleaning operations automatically.

## Example

Messy data:

Name, Age , City  
Dia ,20 , Delhi  
Rahul, ,Mumbai  
Dia ,20 , Delhi  

Cleaned data:

name,age,city  
Dia,20,Delhi  
Rahul,,Mumbai  

## Technologies Used
- Python
- Pandas

## How to Run

Install dependencies:
- pip install pandas

Run the program:
- python main.py
- Enter the path to the CSV file when prompted.

## Future Improvements
- Option to save cleaned file automatically
- Command-line cleaning options
- Data quality summary report