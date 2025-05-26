# 📝 Registration System Using Django

A simple user registration and login system built using the Django framework. This project includes basic authentication features such as sign-up, login, and logout with session management.

---

## 📁 Project Structure

Directory structure:

    ├── README.md
    ├── manage.py
    ├── app1/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── __pycache__/
    │   └── migrations/
    │       ├── __init__.py
    │       └── __pycache__/
    ├── registration/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── __pycache__/
    └── templates/
        ├── home.html
        ├── login.html
        └── signup.html


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shravaniraut175/registration-system-using-django.git
cd registration-system-using-django
```

### 2. Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install django
```

### 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```
python manage.py runserver
Open your browser and go to: http://127.0.0.1:8000
```

---

## 🔐 Features
✅ User Sign-Up

✅ User Login/Logout

✅ Session Management

✅ Basic Form Validation

✅ Simple Frontend using HTML templates

---

## 📸 Screenshots
- Home Page
![Home Page](https://github.com/user-attachments/assets/254a02af-10b7-4155-b8b9-c22731a55b78)


-SignUp Page
![Signup Page](https://github.com/user-attachments/assets/52da0f74-3f8a-4215-a39a-a41aa032cdd5)


- Login Page
![Login Page](https://github.com/user-attachments/assets/c72931ae-87ee-4c38-90f2-0decd31f6ec8)

---

## 🧠 How It Works
Sign-Up: New users can register through signup.html. Upon successful registration, user credentials are saved.

Login: Registered users log in via login.html. Django’s session framework manages user sessions.

Home: After logging in, users are redirected to the home.html page.

Logout: Clicking logout ends the user session and redirects to the login page.

---

## 🛠 Files to Check
File	                  | Description
views.py	              | Contains logic for signup, login, logout, and home views
urls.py (project & app)	| Routing for the application
settings.py	            | Middleware, template dirs, and app registration
templates/*.html	      | User interface templates


---

## 🧑‍💻 Author

Shravani

[GitHub Profile](https://github.com/shravaniraut175)

---

## 📄 License

This project is open source and available under the MIT License.
