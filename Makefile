CONDA_ENV_NAME ?= anaconda-eats

environment:
	conda env create -f environment.yml --name $(CONDA_ENV_NAME) --force

flask:

django: 

angular: 
