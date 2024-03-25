#!/bin/bash

# Displaying pip help
echo "Pip Help"
python3.9 -m pip freeze
python3.9 --version

# Starting build process
echo "BUILD START"

# Installing dependencies
python3.9 -m pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Making migrations
echo "Make Migration"
python3.9 manage.py makemigrations --noinput || { echo "Failed to make migrations"; exit 1; }
python3.9 manage.py migrate --noinput || { echo "Failed to migrate database"; exit 1; }

# Collecting static files
echo "Collect Static"
python3.9 manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

echo "Build process completed successfully"
