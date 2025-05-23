# LinkUp - Social Media Platform (Backend)

![Django](https://img.shields.io/badge/Django-3.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.12-red)

LinkUp is a modern social media platform backend built with Django REST Framework, providing robust APIs for user authentication, posts, and social interactions.

## Features

- **JWT Authentication** (Register, Login, Logout)
- **User Profiles** with profile pictures
- **Post Management** (Create, Read, Update, Delete)
- **Media Uploads** (Images/Videos)
- **Follow/Unfollow** functionality
- **CORS Support** for frontend integration
- **PostgreSQL** database support

## Project Structure
```
backend/ 
├── core/ # Main Django project
│ ├── settings.py # Project configuration
│ ├── urls.py # Main URL routing
│ └── ...
├── accounts/ # User authentication app
│ ├── models.py # Custom User model
│ ├── serializers.py # User serializers
│ └── ...
├── post/ # Posts functionality
│ ├── models.py # Post model
│ ├── views.py # Post viewsets
│ └── ...
├── manage.py # Django management script
└── requirements.txt # Python dependencies
```
## Prerequisites

- Python 3.10+
- PostgreSQL 13+
- pip 20+

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/emmanuelronoh/LinkUp-backend.git
   cd LinkUp-backend/backend
   ```
2. **Set up virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configure environment variables

1. **Create .env file in backend/core/ with:**

  ```bash
   DATABASE_URL=postgres://user:password@localhost:5432/linkup
   SECRET_KEY=your-secret-key-here
   DEBUG=True
  ```

2. **Run migrations**:

```bash
 python manage.py migrate
```

3. **Create superuser**:

  ```bash
   python manage.py createsuperuser
  ```
4. **Running the Server**

  ```bash
    python manage.py runserver
  ```

The API will be available at http://localhost:8000/api/

## API Endpoints

| Endpoint               | Method | Description                  |
|------------------------|--------|------------------------------|
| `/api/auth/register/` | POST   | User registration            |
| `/api/auth/login/`    | POST   | User login (JWT tokens)      |
| `/api/auth/logout/`   | POST   | User logout                  |
| `/api/posts/`         | GET    | List all posts               |
| `/api/posts/`         | POST   | Create new post              |
| `/api/posts/<id>/`    | GET    | Retrieve specific post       |
| `/api/users/`         | GET    | List all users               |
| `/api/users/<id>/`    | GET    | Retrieve specific user profile |


## Configuration

Edit `core/settings.py` to configure:

### Database Settings
```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Security
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'api.yourdomain.com']

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://yourfrontend.com",
    "https://www.yourfrontend.com"
]
```
## Deployment

### Production Checklist

1. **Environment Configuration**:
    ```bash
    # In your .env file
    DEBUG=False
    SECRET_KEY=your-production-secret-key
    ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
    DATABASE_URL=postgres://prod_user:strongpassword@prod-db-host:5432/prod_db
    ```

## Contributing

1. **Fork the repository**

2. **Create your feature branch**
    ```bash
    git checkout -b feature/fooBar
    ```

3. **Commit your changes**
    ```bash
    git commit -am 'Add some fooBar'
    ```

4. **Push to the branch**
    ```bash
    git push origin feature/fooBar
    ```

5. **Create a new Pull Request**
