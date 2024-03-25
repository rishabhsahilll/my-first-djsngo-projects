#!/bin/bash

echo "Pip Help"
python3.9 pip freeze
python3.9 --version

echo "BUILD START"
python3.9 -m pip install Django
python3.9 -m pip install psycopg2-binary
python3.9 -m pip install django-environ
python3.9 -m pip install cloudinary

echo "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic

echo "Build process completed"
