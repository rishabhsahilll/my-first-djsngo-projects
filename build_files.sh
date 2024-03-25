#!/bin/bash

echo "Pip Help"
python3.9 -m pip freeze
python3.9 --version

echo "BUILD START"
python3.9 -m pip install -r requirements.txt

echo "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic --noinput

echo "Build process completed"
