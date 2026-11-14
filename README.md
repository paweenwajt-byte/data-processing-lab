# OOP Data Processing

## Lab Overview
This lab refactors procedural CSV data processing code into an Object-Oriented Programming (OOP) design in Python. It encapsulates file loading and tabular operations (filtering and aggregation) into reusable classes.

## Project Structure
```text
python_work/
├── README.md              # Project documentation
├── Cities.csv             # Cities dataset
└── data_processing.py     # OOP implementation and test script
```

## Design Overview

### DataLoader
Handles reading CSV files from the local filesystem.
- **Attributes:** `base_path` (Path)
- **Key Methods:** `__init__(base_path=None)`, `load_csv(filename)`

### Table
Represents a collection of data rows and supports querying operations.
- **Attributes:** `table_name` (str), `table` (list[dict])
- **Key Methods:** `__init__(table_name, table)`, `filter(condition)`, `aggregate(aggregation_function, aggregation_key)`

## How to Test and Run
```bash
python3 data_processing.py
```
