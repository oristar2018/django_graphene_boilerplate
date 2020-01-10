
include .env


## -----------------------------
## Commands
## -----------------------------

install:
	cp .env.dist .env
	pip install -r requirements.txt

start:
	docker-compose up 

start.docker:
	$(MAKE) migrate
	python manage.py runserver 0.0.0.0:8000

create.superuser:
	python manage.py createsuperuser

migrate_products:
	python manage.py runscript migrate_products

migrate: # migrate database 
	python manage.py makemigrations 
	python manage.py migrate
	$(MAKE) migrate_products


