# cw_5 Project

This is a Django project named **cw_5** that includes a posts application for managing posts with user authentication features.

## Project Structure

```
cw_5
├── manage.py
├── cw_5
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd cw_5
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser** (for accessing the admin site):
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage posts.
- Use the following endpoints for post management:
  - `GET /posts/` - List all posts
  - `GET /posts/my` - List posts by the authenticated user
  - `GET /posts/<id>` - Retrieve a specific post
  - `POST /posts/` - Create a new post
  - `DELETE /posts/<id>/delete` - Delete a specific post

- User authentication endpoints:
  - `GET /login/` - Display login form
  - `POST /login/` - Handle login
  - `GET /logout/` - Handle logout

## License

This project is licensed under the MIT License.