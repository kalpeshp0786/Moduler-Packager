# Multi-Utility Toolkit

## Project Description

Multi-Utility Toolkit is a Python-based console application that provides different useful operations in one program.

This project uses Python built-in modules like `datetime`, `math`, `random`, `time`, and `uuid`. It also uses custom modules `math_utils` and `file_utils` for mathematical and file operations.

The program has a main menu from where the user can select different utility operations.

## Features

### 1. Datetime and Time Operations

This section provides different date and time operations:

- Display current date and time
- Calculate difference between two dates
- Format date into a custom format
- Stopwatch
- Countdown Timer

### 2. Mathematical Operations

This section performs mathematical calculations:

- Calculate factorial
- Calculate compound interest
- Trigonometric calculations
- Calculate area of:
  - Circle
  - Rectangle
  - Triangle

### 3. Random Data Generation

This section generates random data:

- Generate random number
- Generate random list
- Create random password
- Generate random OTP

### 4. Generate Unique Identifiers

This section uses the Python `uuid` module:

- Generate a UUID4
- Generate multiple UUIDs

### 5. File Operations

This section uses the custom `file_utils` module:

- Create a new file
- Write data to a file
- Read data from a file
- Append data to a file

### 6. Explore Module Attributes

This option uses Python's `dir()` function to display the available attributes of selected modules.

Available modules:

- math
- random
- datetime
- time
- uuid
- math_utils
- file_utils

## Technologies Used

- Python
- `datetime`
- `math`
- `random`
- `time`
- `uuid`
- Custom Python Modules
- `dir()` function

## Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
│
└── utility_package/
    ├── __init__.py
    ├── math_utils.py
    └── file_utils.py
```

## How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python version:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the terminal or command prompt inside the project folder.

### Step 3: Run the Program

```bash
python main.py
```

## Main Menu

When the program starts, it displays:

```text
===========================
Welcome to Multi-Utility Toolkit
===========================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
===========================
Enter your choice:
```

Enter the number according to the operation you want to perform.

## Python Concepts Used

This project uses the following Python concepts:

- Functions
- Conditional statements
- `while` loops
- `for` loops
- User input
- Exception handling using `try-except`
- Built-in modules
- Custom modules
- Functions from custom modules
- Lists
- String formatting
- `datetime`
- Random number generation
- UUID generation
- File handling
- `dir()` function

## Custom Modules

### math_utils

The `math_utils` module is used for mathematical operations such as:

- Factorial
- Compound Interest
- Circle Area
- Rectangle Area
- Triangle Area
- Random Password Generation

### file_utils

The `file_utils` module is used for file operations such as:

- Creating files
- Writing files
- Reading files
- Appending data to files

## Error Handling

The program uses `try-except` blocks to handle invalid inputs.

For example:

```text
Invalid input!
```

or:

```text
Invalid date format!
```

This prevents the program from stopping suddenly when the user enters incorrect data.

## Conclusion

The Multi-Utility Toolkit is a simple Python project that combines different useful operations into one console-based application.

It helps demonstrate the use of Python built-in modules, custom modules, functions, loops, conditions, file handling, exception handling, and user input.