# Tattoo artist portfolio website
Powered by Django & Python

## General idea

This is an Tattoo artist website. <br />
Login with your SuperUser.<br />
Go to * [Live](https://uvxts.herokuapp.com/) to see the result 


## Usefull Commands

* Install virtual environment<br />
`$ pip install pipenv`

* Run virtual environment<br />
`$ pipenv shell`

* Install pipfile, pipfile.lock, requirements.txt at once<br />
`$ pipenv install`

* Check if all requirements are installed<br />
`$ pip list`

![Dependencies](img/pip_list.png?raw=true "Pip list")

* To start project you must make migrations<br />
`$ python (or python3) manage.py makemigrations`<br />
`$ python (or python3) manage.py migrate (will migrate all at once)`

* Create SuperUser (admin)<br />
`$ python manage.py createsuperuser`


* Run server<br />
`$ python manage.py runserver`

## Deployment of Python Django Application on Heroku

* Login to heroku<br />
`$ heroku login`<br />
`$ heroku keys:add`

* Create heroku<br />
`$ heroku create`

* to deploy application to Heroku using Git commands<br />
`$ git init`
`$ git add -A`
`$ git commit -m “Initial Commit”`
`$ git push heroku master`

* To start project in heroku you must make migrations<br />
`$ heroku run python manage.py migrate`<br />
`$ heroku run python manage.py createsuperuser`


* Setting enviroment variables<br />
`$ heroku config:set EMAIL_ID='****@gmail.com*'`<br />
`$ heroku config:set EMAIL_PASS='******************`