
#!/usr/bin/env bash
# Build script for Render
set -o errexit

# Install dependencies
pip install -r requirements_production.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate