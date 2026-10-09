# Ekalavya Universys Website

A Django-based educational website for Ekalavya Universys. The application provides structured learning journeys, career guidance, educational resources, expert reviews, contact functionality, and content management through Django Admin.

## Technology Stack

- **Language:** Python
- **Backend:** Django 4.2
- **Database:** MySQL (default configuration) or SQLite (when explicitly configured)
- **Frontend:** HTML5, CSS3, JavaScript
- **Image processing:** Pillow
- **Database connectivity:** PyMySQL
- **Environment configuration:** python-dotenv
- **Static file handling:** WhiteNoise
- **Optional application server:** Gunicorn
- **Production web server:** Existing deployment uses Apache2 with mod_wsgi; verify the target server configuration before deployment.

## Project Structure

```text
ekalavya_project/
├── ekalavya/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── website/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── navigation.py
│   ├── templatetags/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── components/
│   ├── partials/
│   └── ...
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── media/                 # Uploaded content; preserve separately
├── manage.py
├── requirements.txt
├── README.md
└── .env.example
```

Additional local directories such as `venv/`, `__pycache__/` and `staticfiles/` may exist. They are not all source files and should not automatically be included in a deployment archive.

## Prerequisites

- Python 3.11 or another Python version verified against the target environment
- MySQL server for the default database configuration, or SQLite for an explicitly configured local setup
- Git, if cloning the repository

The development environment used during the latest checks was Python 3.11.9 and Django 4.2.30. Confirm the Python version supported by the target AWS environment before deployment.

## Installation

Clone the repository:

```bash
git clone https://github.com/abhay2734/ekalavya-universys-website.git
cd ekalavya-universys-website
```

Create a virtual environment:

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
```

## Environment Configuration

Create a private `.env` file in the project root using `.env.example` as a reference.

The application reads configuration from environment variables. Do not commit real credentials, production secrets or database passwords to Git.

### Example: MySQL

```dotenv
SECRET_KEY=replace-with-a-private-secret
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.mysql
DB_NAME=ekalavya_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

The MySQL database and database user must already exist, with appropriate permissions.

### Example: SQLite for local development

```dotenv
SECRET_KEY=replace-with-a-private-development-secret
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

These examples are alternatives, not values to combine blindly. The application settings determine which database configuration is active.

Use a unique, private `SECRET_KEY` in each environment. Never reuse a publicly disclosed secret in production.

## Database Setup

Check the application configuration:

```bash
python manage.py check
python manage.py showmigrations
```

Apply migrations only after confirming the intended database and taking a suitable backup:

```bash
python manage.py migrate
```

For an existing production installation, preserve the database and inspect pending migrations before applying them. Do not delete migration files or reset the production database as part of routine deployment.

Create an administrator account when needed:

```bash
python manage.py createsuperuser
```

## Running Locally

Start the development server:

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

Run the standard Django check:

```bash
python manage.py check
```

Run the project's tests when appropriate:

```bash
python manage.py test
```

## Static Files

The project uses the following configuration:

- `STATIC_URL = '/static/'`
- `STATICFILES_DIRS` includes the root `static/` directory.
- `STATIC_ROOT` points to `staticfiles/`.
- WhiteNoise is configured to serve collected static assets.

Collect static files when preparing a deployment:

```bash
python manage.py collectstatic --noinput
```

Run this only in the intended environment and after checking the configuration. The `staticfiles/` directory is generated output and can be rebuilt; the source `static/` directory must be preserved.

## Media Files

The application uses `media/` as its media storage directory.

Media files may include images, videos and other content uploaded through Django Admin.

- Preserve existing media when redeploying.
- Back up media before replacing or moving files.
- Do not assume that media is included in Git or in the source ZIP.
- Verify that the production web server can serve uploaded media using the existing configuration.

## Production Deployment

The previously documented production architecture uses Ubuntu, Apache2 and mod_wsgi. Confirm the actual target instance and virtual-host configuration before deployment.

A controlled redeployment should include:

1. Back up the production database and important uploaded media.
2. Confirm the intended application directory and domain.
3. Transfer the verified application source.
4. Preserve the production `.env` and configure it securely.
5. Recreate the Python environment on Linux using the verified dependencies.
6. Run Django checks using the production configuration.
7. Inspect pending migrations and apply only the intended migrations.
8. Collect and validate static assets.
9. Restart or reload the correct application service.
10. Verify the website, admin, static files, media and logs.

Production settings should use `DEBUG=False`, an appropriate `ALLOWED_HOSTS` value, HTTPS, secure cookies and correctly configured proxy headers.

Do not overwrite the existing application directory, database or media files without a verified backup and rollback plan.

Gunicorn is included as a dependency, but it should only be configured as an application server if that matches the chosen production architecture. Do not introduce a new server architecture merely because the package is installed.

## Main Website Features

- Home page and learning journeys
- CLARITY
- SMART IDEA
- CAPABILITY
- CAREER
- FREE TRAINING
- Expert reviews
- Contact Us
- Dynamic footer and administrative content
- Django Admin content management
- Responsive frontend pages

The precise content and availability of each section depend on the current application code and configured database content.

## Security and Maintenance

- Keep `.env` out of Git and ordinary deployment archives.
- Never publish database credentials, API keys or Django secret keys.
- Keep production database backups separate from the application package.
- Preserve all required migration files.
- Do not copy Windows virtual environments to Linux.
- Review dependency updates before applying them to production.
- Test the deployment in a suitable environment before changing the live website.

## License

Proprietary. Use and distribution are subject to the project owner's authorization.