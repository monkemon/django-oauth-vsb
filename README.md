# django-oauth-vsb
Project for VSB 


# running locally
### using docker compose
- make sure you have docker and docker-compose installed
- `mkdir django-oauth`
- `cd django-oauth`
- `git clone https://github.com/monkemon/django-oauth-vsb.git`
- `mv ./docker-compose.yml ./nginx ..`
- `cd ..`
- `docker compose up -d --build`
- the app should run at localhost:8000
- if necessary/or commented out, uncomment ports option in docker-compose.yml



### using python locally
- make sure you have atleast python 3.11
- go to project root
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `cd ./src/oauth2-django-vsb`
- `python manage.py runserver`
- in browser, go to `localhost:8000` (the default django port)
