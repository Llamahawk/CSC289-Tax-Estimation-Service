release: python calculator_project/manage.py migrate
web: gunicorn calculator_project.wsgi
heroku ps:scale web=1