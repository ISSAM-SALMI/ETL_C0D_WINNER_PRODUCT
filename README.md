# ETL Project: Finding the Winner Product

## Objective

The goal of this ETL (Extract, Transform, Load) project is to identify the "winner product" by analyzing products that are diminishing in stock. The pipeline extracts data from a web source, transforms it into a CSV format, and loads it into a MySQL database for further analysis.

## Project Structure

The project consists of the following scripts:

- `COD_GET_DATA.py`: Extracts data from the website using Selenium.
- `Transform.py`: Transforms JSON data into CSV format.
- `Load_Data.py`: Loads CSV data into a MySQL database.
- `ETL.py`: The main script to execute the ETL process.

## Prerequisites

- Python 3.8.2
- MySQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ISSAM-SALMI/ETL_C0D_WINNER_PRODUCT.git
   cd ETL_C0D_WINNER_PRODUCT
   ```

2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your MySQL database and update the connection details in `main.py`.
4. Write your username and password when the browser appears, then click 'OK' in the terminal.
5. Run the code every 5 hours or every 3 hours
6. You can Of course automate this task with Unix/Linux with Crontab

## Usage

1. Run the main script to start the ETL process:
   ```bash
   python ETL.py
   ```

## Details

### Extraction

The extraction process scrapes product data from a specified website using Selenium. The data is saved as JSON files, one for each country.

### Transformation

The transformation process reads the JSON files, extracts relevant information such as price and commission, and saves the transformed data as CSV files.

### Loading

The loading process reads the CSV files and inserts the data into a MySQL database. This enables further analysis to determine which products are diminishing in stock.

## Requirements

Create a `requirements.txt` file with the following content:

```
undetected-chromedriver
selenium
pandas
mysql-connector-python
```
