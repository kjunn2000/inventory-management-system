# Inventory Management System 
## Tech Stack

- **Python:** v3.11
- **Database:** MySQL 8.0
- **IDE:** PyCharm Community Edition v2023.3.2

## Project Setup Guide

This guide provides step-by-step instructions to successfully set up the system for development and testing. Ensure that you follow each step in order.

## Prerequisites

1. Install Python:
   - Download and install Python from [python.org](https://www.python.org/).

2. Install Docker:
   - Ensure Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/).

## Setup Steps

### 1. Clone the Project Repository:

```bash
git clone git@github.com:kjunn2000/inventory-management-system.git
````

After cloned the project, change directory to the folder.

```bash
cd inventory-management-system 
````

### 2. Start Docker Compose:

Run the docker-compose.yml to set up the MySQL database instance and initialize the table schema.

```bash
docker-compose up
```

### 3. Create and Activate a Virtual Environment:

Activating the virtual environment isolates project dependencies.

```bash
python -m venv venv      # Create a virtual environment
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Unix or MacOS
```

### 4. Install Project Dependencies:

Some dependencies are used in this project including requests, mysql-connector-python, coverage and python-dotenv

```bash
pip install -r requirements.txt  # Install project dependencies
```

### 5. Install Project in Editable Mode:

```bash
pip install -e . # Install the project in editable mode
```
# How to run it

## Feature 1 - Create or Update Item Feature

This script is used for creating or updating items. You can modify the request from the file create_update_item_script.py.

```bash
python .\scripts\create_update_item_script.py
```
### Request
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_7.png?raw=true)
### Response
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_6.png?raw=true)


## Feature 2 - Create or Update Item Feature

This script is search the items by last updated datatime. You can modify the request from the file search_items_script.py.

```bash
python .\scripts\search_items_script.py 
```
### Request
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_9.png?raw=true)
### Response
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_11.png?raw=true)

## Feature 3 - Aggregation on the Data by passing in a Category 

This script is aggregate category data and return it with total count for each category. You can modify the request from the file search_cateogry_script.py.

```bash
python .\scripts\search_cateogry_script.py  
```
### Request
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_5.png?raw=true)
### Response
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_10.png?raw=true)

# How to test it
## 1. Run Unit Tests:

This command runs unit tests for the project. There are a total number of 53 test cases.

```bash
python -m unittest discover .\tests\unit\
```

After run the script above, you should expect to see the below result.

![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_13.png?raw=true)

## 2. Generate and View Code Coverage Report:

This generates and displays a code coverage report for the unit tests. By run the attached script, you should get similar result (100% code coverage).
There are one folder that state at below will be excluded from the test coverage report
1) dao, since the purpose it exists is interacting with database, it is best practice to test it as integration test with a mock database.

```bash
python -m coverage run --omit="*/dao/*" -m unittest discover .\tests\unit\
```
![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_2.png?raw=true)

```
python -m coverage report
```

![alt text](https://github.com/kjunn2000/inventing_management_system_readme_image/blob/main/img_3.png?raw=true)
