# anaconda-eats
Welcome to the greenfield coding portion of your interview at Anaconda! Today, you will be building a platform called "Anaconda Eats", which is intended to be a place on the internet where users can store and retrieve recipes that they want to use later.

# First Steps
1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo, so that you can access the prompts and some handy automation we've set up to ease the process.
2. Check the `prompts` directory to find interview prompts specific to your position. They are linked below for your convenience:
    * [Backend Engineer Prompt](prompts/prompt_backend.md)
    * [Frontend Engineer Prompt](prompts/prompt_frontend.md)
    * [Fullstack Engineer Prompt](prompts/prompt_fullstack.md)
    * [QA Engineer Prompt](prompts/prompt_qa.md)
3. Ask questions! *Please* ask any questions you have. We believe the best programming is a collaborative process, and interviews should be too! Feel free to reach out if there is anything unclear about the task, or if any issues arise that you'd like clarification on.
4. (optional) Use the gitpod instance and/or Makefile we've included in this repo to create an environment for this interview. See below for more details.
5. Start programming! 

## Creating and Using the Preconfigured Environment
* A [Gitpod instance](https://gitpod.io/#https://github.com/anaconda-interviews/anaconda-eats) has been configured for this repo, which creates a Linux environment with options for various Python-based full-stack/BE web servers when started. Candidates can use this instance to create and run any files/projects they want for their prompt. If you are forking this repo to your own, you can access a gitpod instance by prepending `gitpod.io/#` to the url of your forked repo, e.g. type `gitpod.io/#https://github.com/your-github-fork/anaconda-eats` in your web browser address bar to start an instance. You may be asked to link gitpod to your GitHub account. The Gitpod instance is not a requirement for the interview, it's just meant to make your process a bit easier.

* To jumpstart your process, take a look at the `Makefile` for `make` commands that will create cookiecutter projects in the platform of your choice. For example, once you have started the gitpod and received the message "Ready to begin!", typing `make fastapi` will create an environment and run a basic [FastAPI](https://fastapi.tiangolo.com/) app that you will then be able to iterate on.


## Tips & Tricks for your Interview
- Explain the approach you are intending to take and be sure to document any assumptions you made. 
- Be sure to tell us what your priorities are when it comes to application so we know what you focused on and where you'd improve given more time.
- If you would like to test things on an example backend, an API with Swagger docs is available [here](http://anacondaeats.pythonanywhere.com/).

## Requirements
- Please add a README that explains how to get your application up and running.
- Make sure that you've gone through and tested that everything you've made works.