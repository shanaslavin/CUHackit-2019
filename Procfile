release: python manage.py migrate
web: gunicorn Hackit.wsgi --log-file -
web: gunicorn Hackit.asgi:application --log-file -
