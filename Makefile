CONDA_ENV_NAME ?= anaconda-eats

aiohttp:
	conda install -y aiohttp -c conda-forge
	cd templates/aiohttp && python -d -m aiohttp.web -H localhost -P 8080 app:start_app

bottle:
	conda install -y bottle -c conda-forge
	cd templates/bottle && python app.py

django:
	conda install -y django -c conda-forge
	cd templates/django && django-admin startproject example \
	&& cd example && python manage.py runserver

environment:
	conda env create -f environment.yml --name $(CONDA_ENV_NAME) --force

fastapi:
	conda install -y fastapi uvicorn-standard -c conda-forge
	cd templates/fastapi && uvicorn app:app --reload

flask:
	conda install -y flask -c conda-forge
	cd templates/flask && flask --app app run

quart:
	conda install -y quart -c conda-forge
	cd templates/quart && python app.py

tornado:
	conda install -y tornado -c conda-forge



