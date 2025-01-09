#!/bin/bash
source /home/askar/code/django-app/env/bin/activate
exec gunicorn  -c "/home/askar/code/django-app/gunicorn_config.py" config.wsgi