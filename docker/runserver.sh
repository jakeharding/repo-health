#!/bin/bash
echo "DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'msr14',
        'USER': 'msr14',
        'PASSWORD': 'msr14',
        'HOST': 'database',
        'PORT': '3306'}}" > repo_health/local_settings.py

until nc -z -v -w30 'database' 3306
do
  echo "Waiting for connection to database..."
  # wait for 7 seconds before checking if DB is up
  sleep 7
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000