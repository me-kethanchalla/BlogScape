# BlogScape

Welcome to **BlogScape**! This is **Kethan Challa** and this project is a blog platform where users can create and search for blogs, view other authors, and manage their profiles.

## Features
- User registration and login
- Profile management
- Blog creation, search, and detailed view
- Author search and profile navigation

## Table of Contents
1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)

## Getting Started

These instructions will guide you through setting up **BlogScape** on your local machine for development and testing purposes.

## Prerequisites

Ensure you have the following installed on your machine:
- **Python 3.x**.
- **pip**: Python package installer.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/me-kethanchalla/BlogScape.git
    ```

2. **Navigate to the project directory**:
    Navigate inside the cloned directory and then navigate to another directory inside using

   ```bash
    cd BlogScape
    ```

3. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install Django**:

    Django is the web framework that powers **BlogScape**. Install it with the following command:

    ```bash
    pip install django
    ```

8. **Install Django Crispy Forms**:

    This project uses **crispy forms** to handle form styling. Install it by running:

    ```bash
    pip install django-crispy-forms
    ```

9. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

10. **Visit the site**:

    Open your browser and go to `http://127.0.0.1:8000/` to view your site.


## NOTE :

#### If you have made any changes in the models or forms structures.

 **Make migrations and migrate the database**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

#### If you need to access the admin view
 **Create a superuser (admin)**:

    ```bash
    python manage.py createsuperuser
    ```


