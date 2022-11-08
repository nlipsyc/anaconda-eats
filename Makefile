CONDA_ENV_NAME ?= anaconda-linter

environment:
	conda env create -f environment.yml --name $(CONDA_ENV_NAME) --force
