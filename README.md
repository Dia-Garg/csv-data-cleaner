# CSV Data Cleaner

A Python automation tool that cleans messy CSV files and prepares them for further data processing.

The script loads a CSV file, performs common cleaning operations, and allows the user to export a cleaned version of the dataset.

---

## Features

- Removes extra whitespace from text cells
- Removes completely empty rows
- Removes duplicate rows
- Displays original and cleaned data preview
- Allows the user to save the cleaned dataset to a new file

---

## Example

### Input CSV


Name, Age , City
Dia , 20 , Delhi
Rahul, , Mumbai
, ,
Dia , 20, Delhi


### Output After Cleaning


Name,Age,City
Dia,20,Delhi
Rahul,,Mumbai


---

## Technologies Used

- Python
- Pandas

---

## Installation

Install the required library:


pip install pandas


---

## How to Run

Run the script:


python main.py


Then provide the CSV file path when prompted.

Example:


Enter CSV file name: sample_data.csv


After cleaning, the program will ask where to save the cleaned file.

---

## Project Structure


csv-data-cleaner
│
├── main.py
├── sample_data.csv
└── README.md


---

## Future Improvements

- Allow users to choose specific cleaning operations
- Generate a cleaning report (rows removed, duplicates removed)
- Support large datasets efficiently