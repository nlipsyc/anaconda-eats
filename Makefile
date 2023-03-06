CONDA_ENV_NAME ?= anaconda-eats

aiohttp:
	conda install -y aiohttp
	cd templates/aiohttp && python -d -m aiohttp.web -H localhost -P 8080 app:start_app

bottle:
	conda install -y bottle
	cd templates/bottle && python app.py

django:
	conda install -y django
	cd templates/django && django-admin startproject example \
	&& cd example && python manage.py runserver

environment:
	conda env create -f environment.yml --name $(CONDA_ENV_NAME) --force

fastapi:
	conda install -y fastapi uvicorn-standard
	cd templates/fastapi && uvicorn app:app --reload

flask:
	conda install -y flask
	cd templates/flask && flask --app app run

quart:
	conda install -y quart
	cd templates/quart && python app.py

tornado:
	conda install -y tornado



