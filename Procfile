web: gunicorn --bind 0.0.0.0:$PORT volcano:app
python manage.py collectstatic --noinput
manage.py migrate