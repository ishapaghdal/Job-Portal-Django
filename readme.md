# Job Listing Portal

A web application for managing job postings, built using Django, Css and Bootstrap. This application allows companies to manage their jobs.

## Features

- **User Authentication**: 
  - login and registration system.and company users.
  - user can register their compnay.

- **Job Management**:
  - Companies can create, edit, and delete job postings.
  - Job listings include titles, descriptions and other related details.

- **Pagination**:
  - Job listings are paginated for better user experience.
  - Bootstrap-styled pagination for easy navigation.


## Installation

Follow these steps to set up the project on your local machine:


### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ishapaghdal/Job-Portal-Django.git
   cd Job-Portal-Django

2. **Install Dependencies**:
   ```bash
    pip install -r requirements.txt
3. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Run the Server:**
    ```bash
    python manage.py runserver
