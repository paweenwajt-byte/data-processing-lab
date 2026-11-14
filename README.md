# OOP Data Processing

## Lab Overview
This lab refactors procedural CSV data processing code into an Object-Oriented Programming (OOP) design in Python. It encapsulates CSV file loading, database table management, and tabular query operations (filtering, aggregation, and table joins) into reusable classes.

## Project Structure
```text
python_work/
├── README.md              # Project documentation
├── Cities.csv             # Cities dataset
├── Countries.csv          # Countries dataset
└── data_processing.py     # OOP implementation and test script
```

## Design Overview

### DataLoader
Handles reading CSV files from the local filesystem.
- **Attributes:** `base_path` (Path)
- **Key Methods:** `__init__(base_path=None)`, `load_csv(filename)`

### DB
Represents an in-memory database managing multiple `Table` objects.
- **Attributes:** `tables` (list[Table])
- **Key Methods:** `__init__()`, `insert(table)`, `search(table_name)`

### Table
Represents a collection of data rows and supports querying, aggregation, and relational join operations.
- **Attributes:** `table_name` (str), `table` (list[dict])
- **Key Methods:** `__init__(table_name, table)`, `filter(condition)`, `aggregate(aggregation_function, aggregation_key)`, `join(other_table, common_key)`, `__str__()`

## How to Test and Run
```bash
python3 data_processing.py
```
