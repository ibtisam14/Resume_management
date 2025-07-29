# Django Resume System

This is a Django-based project that includes:

- Custom user model with email login
- JWT Authentication using `djangorestframework-simplejwt`
- User registration & login
- Admin seeder
- Swagger API docs via `drf-yasg`
- resume management

---

## 🚀 Features

- Custom `User` model with email as `USERNAME_FIELD`
- JWT authentication with custom payload
- Admin user seeding with `python manage.py run_seeders`
- Swagger UI auto-generated documentation
- Clean modular code with serializers, views, and commands

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ibtisam14/Resume_management
cd system_management
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Seed the admin user

```bash
python manage.py run_seeders
```

---

## 🔑 Authentication

- **Register**: `POST /api/register/`
- **Login** (JWT): `POST /api/login/`  
  Example credentials:

  ```
  {
    "email": "admin@gmail.com",
    "password": "admin123"
  }
  ```

---

## 🧪 Run Dev Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/swagger/` to test APIs using Swagger UI.

---

## 🗂 Project Structure

```
├── system_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── run_seeders.py
├── manage.py
└── requirements.txt
```

---

## ✅ Dependencies

- Django
- djangorestframework
- djangorestframework-simplejwt
- drf-yasg

---

## 📄 License

MIT License

---

## 👨‍💻 Author

- Developer
