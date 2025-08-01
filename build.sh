#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input --settings config.settings.production

# Apply any outstanding database migrations
python manage.py migrate --settings config.settings.production

# Create Django superuser
# This environment variables MUST be supplied on setup:
# DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --noinput --settings config.settings.production