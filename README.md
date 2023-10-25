# EMPproject
# Employee Attendance and Salary Management System

**Table of Contents**
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [User Guide](#user-guide)
- [Admin Guide](#admin-guide)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

## Project Overview
The Employee Attendance and Salary Management System is a versatile software application designed to streamline the process of recording and managing employee attendance and calculating their salaries. It provides a user-friendly interface for employees to log their attendance and enables administrators to generate attendance and salary reports. The system automates the calculation of regular and overtime salaries based on predefined salary rates. This project leverages Python, PyQt6 for the graphical user interface, MySQL for data storage, and Pandas for data manipulation and export.

## Key Features
- **User-Friendly Interface**: The system boasts an intuitive GUI built with PyQt6, ensuring that employees and administrators can interact with ease.

- **Attendance Management**: Employees can log their attendance by providing their employee ID, name, date, log-in, and log-out times. The system validates entries, checks for duplicate dates, and calculates total working hours, excluding break hours.

- **Admin Access**: Administrators have a specialized view for generating attendance and salary reports. They can retrieve data for specific employees and date ranges.

- **Salary Calculation**: The application automatically calculates regular and overtime salaries based on working hours and predefined salary rates.

- **Data Export**: Admins can easily export attendance and salary data to an Excel file for further analysis and record-keeping.

- **Data Validation**: The system employs data validation techniques to ensure accurate and complete information entry, enhancing data integrity.

## Technologies Used
- **Python**: The core programming language.
- **PyQt6**: Utilized for creating the graphical user interface.
- **MySQL**: Manages the database for storing employee data, attendance records, and predefined salary rates.
- **pandas**: Handles data manipulation and Excel data export.
- **QPalette**: Customizes the application's appearance.

## Installation
[Include detailed installation instructions, including prerequisites and steps to set up the project. You can provide information about database setup, PyQt6 installation, and any other requirements.]

## User Guide
### Logging Attendance
1. Launch the application.
2. Enter your Employee ID, name, date, log-in, and log-out times.
3. Click the "Submit" button.

### Admin Guide
### Generating Reports
1. Enter the Employee ID.
2. Specify the date range by selecting "From Date" and "To Date."
3. Click the "Submit" button.

### Data Export
1. After generating a report, click the "Download" button to export data to an Excel file.

