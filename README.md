# django-oauth-vsb
Project for VSB 


# running locally
### using docker



### using python locally
- make sure you have atleast python 3.11
- go to project root
- `$ python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `cd /src/ouauth`
- `export DJANGO_DEBUG=1`
- `python manage.py runserver`
- in browser, go to `localhost:8000` (the default django port)