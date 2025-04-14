# django-oauth-vsb
Project for VSB 

# deployment
- buy a domain
- buy a hosting
- from server, complete a DNS challenge from providers like Let'sEncrypt
- run Traefik container on the server
- you need both nginx and django-oauth services

# running locally
### using docker compose
- make sure you have docker and docker-compose installed
- `mkdir django-oauth`
- `cd django-oauth`
- `git clone https://github.com/monkemon/django-oauth-vsb.git`
- `mv ./docker-compose.yml ./nginx ..`
- `cd ..`
- the `target` should be set to `debug` in docker-compose
- port 8000 should be mapped to 9999 in docker-compose
- `docker compose up --build django-oauth` // you don't need the nginx for this
- the app should run at localhost:8000


### using python locally
- make sure you have atleast python 3.11
- go to project root
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `cd ./src/oauth2-django-vsb`
- `python manage.py runserver`
- in browser, go to `localhost:8000` (the default django port)
