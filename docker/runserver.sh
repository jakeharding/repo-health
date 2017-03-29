#!/bin/bash

# Create the local_settings.py to connect to the docker mysql
echo "DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'msr14',
        'USER': 'msr14',
        'PASSWORD': 'msr14',
        'HOST': 'database',
        'PORT': '3306'}}" > repo_health/local_settings.py

# Check if the database is done running its init scripts
until nc -z -v -w30 'database' 3306
do
  echo "Waiting for connection to database..."
  # wait for 7 seconds before checking if DB is up
  sleep 7
done

# Migrate and start the server
python manage.py migrate
python manage.py runserver 0.0.0.0:8000