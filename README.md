# Ashutosh_Gautam_assingment
this assingment is to show the user management system
# Flask User Management API

This project is a simple Flask application that connects to a MySQL database and provides basic user management functionalities. It includes routes to list users, add new users, view user details, and provides a simple HTML interface styled with CSS.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Database Setup](#database-setup)
  - [Application Setup](#application-setup)
- [Usage](#usage)
  - [Routes](#routes)
  - [HTML Templates](#html-templates)
  - [Static Files](#static-files)
- [SQL Queries](#sql-queries)
  - [Insert Sample Data](#insert-sample-data)
  - [Retrieve All Users](#retrieve-all-users)
  - [Retrieve a Specific User by ID](#retrieve-a-specific-user-by-id)
- [Additional Notes](#additional-notes)

## Project Structure

/flask-user-management  
│  
├── app.py  
├── /templates  
│ ├── base.html  
│ ├── users.html  
│ ├── new_user.html  
│ └── user_detail.html  
└── /static  
└── styles.css

## Setup

### Database Setup

1. **Create a MySQL database:**

   ```sql
   CREATE DATABASE users;

   ### use user table
   USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

## Application setup  
 - Clone the repository:
   git clone https://github.com/Ashu29y/Ashutosh_Gautam_assingment.git
   cd flask-user-management
 - Install dependencies:
   pip install -r requirements.txt
 - Configure the database connection:
  app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'users'

# SQL Queries 
- Insert sample users into the users table:
  INSERT INTO users (name, email, role) VALUES ('Alice Johnson', 'alice@example.com', 'admin');
  INSERT INTO users (name, email, role) VALUES ('Bob Smith', 'bob@example.com', 'user');
  INSERT INTO users (name, email, role) VALUES ('Charlie Brown', 'charlie@example.com', 'user');
- Retrieve All Users:
  SELECT * FROM users;
- Retrieve a Specific User by ID :
  SELECT * FROM users WHERE id = 1;

## Additional Notes

- Ensure MySQL server is running and accessible.
- The database credentials in app.py should match your MySQL setup.
- Customize the CSS in styles.css to change the appearance of the HTML pages.
