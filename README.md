# Django REST Framework Project

## Description
This repository contains the complete code for a Django REST Framework project, showcasing the implementation of various concepts learned from a comprehensive tutorial playlist. This project manages user registration, login, profile access, and password management using JWT authentication.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [API Overview](#api-overview)
4. [Features](#features)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This project demonstrates the principles of API development using Django REST Framework. It includes various endpoints for managing user data and authentication in a structured way.

## Installation
To run this project, ensure you have Python and Django installed on your machine. Follow these steps to set up the environment:
1. Clone the repository:
   ```bash
   git clone https://github.com/M-Abdullah-Py/Recipe-and-Student-Report-Card-Project.git
   cd Recipe-and-Student-Report-Card-Project
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
Access the API at http://127.0.0.1:8000/api/.

#API Overview
This project includes endpoints for:

Creating, reading, updating, and deleting user profiles.
User registration and login with JWT authentication.
Password reset functionality.
Features
CRUD Operations: Manage user information.
Authentication: Secure API access with JWT.
Password Management: Reset password via email.
Profile Management: Access and update user profiles.
Usage
After running the development server, you can use tools like Postman or your browser to interact with the API endpoints. Documentation for available endpoints is included in the project.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any changes or enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
