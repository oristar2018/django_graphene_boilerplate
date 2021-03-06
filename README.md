# Django graphene boilerplate

This boilerplate uses postgres, django and graphene to provide a flexible backend using gql code first with no schema maintenance.

The ide configuration described is for Vscode

# Requirements

Make sure you have python3 && pip installed.

# Basics

Create a virtual environment using `python3 -m venv .`

Choose python 3.6 interpreter for your venv `ctlr shift p -> Python: Select interpreter -> Python 3.6 (ge or your venv)`

Choose pylint as linter `ctlr shift p -> Python: Select linter`

Add this to your settings.json by typing pylint args in settings preference in vscode

`"python.linting.pylintArgs": [ "--load-plugins=pylint_django", "--disable=C0111" ],`

( the second argument disables useless linting rules for pylint. )

Make sure you have the permissions in the project's directory. If not, run `sudo chown -R $USER:$USER .`

Install your dependencies for local development `pip install -r requirements.txt`

Make sure pylint django is installed `pip install pylint-django`

Use and configure python-dotenv if you need to run this in local outside of docker

## If installing from scratch

delete the django_graphene folder

Run `docker-compose run web django-admin startproject yourprojectname .`

go into your container `docker exec -it djangographene_web_1 sh`

start your app within the project's directory `django-admin startapp myproject`

make sure your app is installed in the installed apps in settings.py in the project's directory

make sure your settings.py has the right database configuration, cors middleware && configuration and graphene configuration

your app's directory must have a models.py / schema.py

your project's directory must have a top level schema.py

your views.py must have your graphql endpoint url

your admin.py must register your models

- examples are found in the base project

## If not installing from scratch

Refactor the projects's and app's name to your liking. Make sure all occurences are changed or it will bug the app

Modify the app/models && schema to begin development

## Launching and parametring the app

Launch the app with `docker-compose up`

go into your container `docker exec -it djangographene_web_1 sh`

Run your migrations with `python manage.py makemigrations` and `python manage.py migrate`

Create a superuser `python manage.py createsuperuser`

Go to `localhost:8000/admin` log in and enter data

Go to `localhost:8000/graphql` and query the basic model

## Common errors

Make sure to use the type and not the models when defining your resolvers
