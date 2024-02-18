#Install required packages for both Django and PostgreSQL adapter
pip install Django psycopg2-binary

#Configure Database settings in the settings.py file of the Django Project
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.oracle',
        'NAME':'scraju_dbhigh',
        'USER':'admin', 
        'PASSWORD':'mypw', #Please provide the db password here
    }
}

#Run migrations
python manage.py makemigrations
python manage.py migrate

#Define models(tables in database) in Django
from django.db import models

class ModelName(models.Model):
    Username = models.CharField(max_length=255)
    Password = models.IntegerField()
    #Add more if needed

#Use Django ORM to interact with Database
from .models import ModelName
data = ModelName.objects.all()

new_record = ModelName(Username='username', Password=1)
new_record.save()

python manage.py runserver
