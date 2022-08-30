
# Django

This Django project shows the basic working and features of Django such as creating and setting up apps, templates, running the app etc.
The following instructions guide you in achieving the above mentioned.



## Deployment

Django project and app

Terminal -

```bash
  django-admin startproject "projectname"
```
IDE -
```bash
  pip install env
  virtualenv "name"

  if virtual environment is not activated 
  r\Scripts\activate.bat 

  git clone git@github.com:llraekll/django.git
  pip install -r requirements.txt

  python manage.py makemigrations #migrations must be made even with the slightest change made in models.py
  python manage.py migrate
  python manage.py runserver

```
