command = '/home/askar/code/django-app/env/bin/gunicorn'
pythonpath = '/home/askar/code/django-app/config'
bind = '127.0.0.1:8001'
workers = 3
user = 'askar'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'