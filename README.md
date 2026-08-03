![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/License-Proprietary-red)

# Ekalavya Universys Website

A production-ready Django-based educational website for Ekalavya Universys, providing structured learning journeys, career guidance, AI-powered educational content, free training resources, and administrative content management through Django Admin.

## Technology Stack

- Python 3.12
- Django 4.2
- MySQL / SQLite (development)
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- WhiteNoise
- Gunicorn

## Installation

```bash
git clone https://github.com/abhay2734/ekalavya-universys-website.git
cd ekalavya-universys-website

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
ALLOWED_HOSTS=
SECRET_KEY=your-secret-key
DEBUG=True
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

For MySQL:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=ekalavya_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

## Database Setup

```bash
python manage.py migrate
```

## Static Files

```bash
python manage.py collectstatic
```

## Running Locally

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

## Production Deployment

- Set DEBUG=False
- Configure ALLOWED_HOSTS
- Configure the .env file
- Run database migrations
- Collect static files
- Configure Gunicorn
- Configure Nginx or Apache
- Enable HTTPS

## Admin Login

```bash
python manage.py createsuperuser
```

## License

Proprietary

## Project Structure

```text
ekalavya/
website/
templates/
static/
media/
manage.py
requirements.txt
```

## Features

- Dynamic Django Admin
- Home Page
- CLARITY
- SMART IDEA
- CAPABILITY
- CAREER
- FREE TRAINING
- AI Expert Reviews
- Contact Us
- Dynamic Footer
- Responsive Design

This website is fully content-managed through Django Admin, allowing administrators to update pages, media, training content, and website settings without modifying the source code.
