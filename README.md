pennua
======

PennUA Website in DjangoCMS

To Deploy:

1. SSH into server
2. Run a git pull
3. `manage.py collectstatic`
4. `sudo service nginx restart && sudo service gunicorn restart`
