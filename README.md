## Overview
A simple HTTP API for a workflow system, The API allow for retrieving, listing, creating, updating and deleting workflows and comments

A workflow is a series of ordered steps to be followed in order to achieve a result. It has a name, a description and a set of ordered steps. A step has a name and a description.

A comment is a message left by someone about a workflow. A comment has the name of the person who posted and the text of the comment.

## Clone and Build
### Requirements
* Python 3.8.2 https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
* Git https://git-scm.com/download/win
 
### Build the project
* Open Command Prompt
* Clone this repository
```commandline
git clone https://github.com/RayanAlbouni/Workflows.git
```
* cd into workflowsproject Folder 
```commandline
cd Workflows
``` 
* Create a virtual environment to isolate our package dependencies locally
```commandline
python -m venv env
env\Scripts\activate
```
* Install Django and Django REST framework into the virtual environment
```commandline
pip install django
pip install djangorestframework
```
* Sync your database for the first time
```commandline
python manage.py migrate
```
* Create an initial user named 'admin' with a password of 'password'
```commandline
python manage.py createsuperuser --email admin@example.com --username admin
```
* Create an initial migration, and sync the database for the first time
```commandline
python manage.py makemigrations workflowsproject
python manage.py migrate
```
* Run the project
```commandline
python manage.py runserver
```

* To run unit test:
```commandline
python manage.py test
```

* To display OpenAPI spec, open the link in your browser:
```
http://127.0.0.1:8000/schema/
```


# How to integrate
* Comment API

```json
{
  "ss": ""
}
```
'''