**Library System**
A simple Library Management System built with Django to manage and display information about books, events, and other library-related data. The system provides an admin interface for managing CRUD (Create, Read, Update, Delete) operations for books and events. The project also uses pipenv for managing dependencies.

**Features**
Book Management: Admin can add, update, delete, and view books in the library.
Event Management: Admin can add, update, delete, and view library events.
Admin Interface: Easy-to-use admin interface for managing the library's books and events.
**Database:**
Data is stored in a relational database, which is managed through Django's ORM.
Pipenv for Dependency Management: Uses pipenv to manage Python dependencies.
**Installation**
Follow these steps to set up the project on your local machine.

**Prerequisites**
Make sure you have the following installed:

Python (>= 3.8)
pipenv (if not already installed, run pip install pipenv)
Steps
Clone the Repository

**bash**
git clone https://github.com/yourusername/library-system.git
cd library-system

**Set Up Virtual Environment**

**Install the dependencies using pipenv:**

**bash**
pipenv install
Apply Migrations

**Run the database migrations to set up the database schema.**

**bash**
pipenv run python manage.py migrate
Create a Superuser

**If you want to access the admin interface, create a superuser.**

**bash**
pipenv run python manage.py createsuperuser

**Follow the prompts to create the admin account.**

**Run the Development Server**

**Start the development server to view the application.**
bash
pipenv run python manage.py runserver
Access the Admin Interface

Visit http://127.0.0.1:8000/admin in your browser. Log in with the superuser credentials to manage the library’s books and events.

![image](https://github.com/user-attachments/assets/00c05e0b-41ff-491f-a661-85afd1f2def6)

![image](https://github.com/user-attachments/assets/d14e9d13-2b1d-419d-af6d-73ab84601c5a)

![image](https://github.com/user-attachments/assets/27dc7210-e711-4e16-9ef0-b594330a27a2)

![image](https://github.com/user-attachments/assets/14c42bab-0f5a-4082-8b34-74aa86fe073f)

![image](https://github.com/user-attachments/assets/2ed9538e-c964-4ccc-894a-84e7d5107a32)

![image](https://github.com/user-attachments/assets/616866f4-0580-48b4-a77d-42d75b169558)








