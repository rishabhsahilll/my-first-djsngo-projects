echo "BUILD START"
python -m pip install -r requirements.txt

echo "Make Migration"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static"
python manage.py collectstatic