# Django Project with JWT Authorization, WebSocket Notifications, and Game Functionality

This project is a Django web application that includes user authentication (registration, login, logout), article management (add, view, delete), game management (add, view, edit, delete), and real-time notifications using WebSockets.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [WebSocket Notifications](#websocket-notifications)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Django Channels
- djangorestframework-simplejwt
- drf-spectacular

## Installation

1. Install pipenv if you haven't already:
    ```bash
    pip install pipenv
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    pipenv install
    ```

3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

4. Apply the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```


## Running the Application

Start the Django development server:
```bash
python manage.py runserver
```

Start the ASGI server using Daphne:
```bash
daphne -p 8000 cms_pavlinov.asgi:application
```

## API Documentation

You can access the API documentation at [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/).

## WebSocket Notifications

The WebSocket endpoint for notifications is located at `ws://127.0.0.1:8000/ws/notifications/`.

## Usage

1. **Registration and Login:**
   - Register a new user at `/register/`.
   - Login with the registered user at `/login/`.

2. **Article Management:**
   - Add a new article at `/article/add/`.
   - View articles at `/articles/`.
   - View a single article at `/article/<id>/`.
   - Delete an article at `/article/<id>/remove/`.

3. **Game Management:**
   - Add a new game at `/game/add/`.
   - View games at `/games/`.
   - Edit a game at `/game/<id>/edit/`.
   - Delete a game at `/game/<id>/remove/`.