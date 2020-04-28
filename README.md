# Overview
A simple HTTP API for a workflow system, The API allow for retrieving, listing, creating, updating and deleting workflows and comments

A workflow is a series of ordered steps to be followed in order to achieve a result. It has a name, a description and a set of ordered steps. A step has a name and a description.

A comment is a message left by someone about a workflow. A comment has the name of the person who posted and the text of the comment.

# Clone and Build
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
* Install Django and Django REST framework into the virtual environment, and pyyaml to generate schema into YAML-based OpenAPI format
```commandline
pip install django
pip install djangorestframework
pip install pyyaml uritemplate
```
* Sync your database for the first time
```commandline
python manage.py migrate
```
* Create an initial user named 'admin' with a password of 'password'
```commandline
python manage.py createsuperuser --email --username admin
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
## Workflow API

##### Create Workflow
To create a new workflow
```
Request Endpoint
POST \workflow\
Headers: content-type:application/json
```

```
Request Body
{
    "name": "How to nail something",
    "description": "Basic instructions to nail something",
    "steps": [
      {
         "name": "Place nail",
         "description": "Hold nail on top the thing to be nailed"
      },
      {
        "name": "Hit nail",
        "description": "Hit the nail repeatedly with a hammer"
      }   
    ]
}
```
```
Respone headers
HTTP/1.1 201 Created

Response Body 
{
   "id":1,
   "name":"How to nail something",
   "description":"Basic instructions to nail something",
   "steps":[
      {
         "name":"Place nail",
         "description":"Hold nail on top the thing to be nailed"
      },
      {
         "name":"Hit nail",
         "description":"Hit the nail repeatedly with a hammer"
      }
   ]
}
```
##### View Workflows
To list all workflows
```
Request Endpoint
GET \workflow\
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
[
   {
      "id":1,
      "name":"How to nail something",
      "description":"Basic instructions to nail something",
      "steps":[
         {
            "name":"Place nail",
            "description":"Hold nail on top the thing to be nailed"
         },
         {
            "name":"Hit nail",
            "description":"Hit the nail repeatedly with a hammer"
         }
      ]
   }
]
```
##### View Workflow Details
To retrieve a workflow by ID
```
Request Endpoint
GET \workflow\:id\
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
{
   "id":1,
   "name":"How to nail something",
   "description":"Basic instructions to nail something",
   "steps":[
      {
         "name":"Place nail",
         "description":"Hold nail on top the thing to be nailed"
      },
      {
         "name":"Hit nail",
         "description":"Hit the nail repeatedly with a hammer"
      }
   ]
}
```
##### Update Workflow
To update a workflow
```
Request Endpoint
PUT \workflow\:id\
Headers: content-type:application/json
```
```
Request Body
{
    "name": "How to nail something [Update]",
    "description": "Basic instructions to nail something",
    "steps": [
      {
         "name": "Place nail",
         "description": "Hold nail on top the thing to be nailed"
      },
      {
        "name": "Hit nail",
        "description": "Hit the nail repeatedly with a hammer"
      }   
    ]
}
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
{
   "id":1,
   "name":"How to nail something [Update]",
   "description":"Basic instructions to nail something",
   "steps":[
      {
         "name":"Place nail",
         "description":"Hold nail on top the thing to be nailed"
      },
      {
         "name":"Hit nail",
         "description":"Hit the nail repeatedly with a hammer"
      }
   ]
}
```
##### Delete Workflow
To delete a workflow
```
Request Endpoint
DELETE \workflow\:id\
Headers: content-type:application/json
```
```
Respone headers
HTTP/1.1 204 No Content
```
## Comment API

##### Create Comment
To create a new workflow
```
Request Endpoint
POST \comment\:workflow_id\
Headers: content-type:application/json
```
```
Request Body
{
  "name": "Concerned  person",
  "text": "On the step 'Hit Nail' be careful to not hit your hand!"
}
```
```
Respone headers
HTTP/1.1 201 Created

Response Body 
{
   "id":1,
   "name":"Concerned  person",
   "text":"On the step 'Hit Nail' be careful to not hit your hand!"
}
```
##### View Comments
To list all comments for a workflow
```
Request Endpoint
GET \comment\:workflow_id\
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
[
   {
      "id":1,
      "name":"Concerned  person",
      "text":"On the step 'Hit Nail' be careful to not hit your hand!"
   }
]
```
##### View Comment Details
To retrieve a Comment by ID
```
Request Endpoint
GET \comment\:workflow_id\:id\
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
{
    "id":1,
    "name":"Concerned  person",
    "text":"On the step 'Hit Nail' be careful to not hit your hand!"
}
```
##### Update Comment
To update a comment
```
Request Endpoint
PUT \comment\:workflow_id\:id\
Headers: content-type:application/json
```
```
Request Body
{
  "name": "Concerned  person [Update]",
  "text": "On the step 'Hit Nail' be careful to not hit your hand!"
}
```
```
Respone headers
HTTP/1.1 200 OK

Response Body 
{
    "id":1,
    "name":"Concerned  person [Update]",
    "text":"On the step 'Hit Nail' be careful to not hit your hand!"
}
```
##### Delete Comment
To delete a comment
```
Request Endpoint
DELETE \workflow\:workflow_id\:id\
Headers: content-type:application/json
```
```
Respone headers
HTTP/1.1 204 No Content
```
## Open API Spec
To access OpenAPI Spec, run the server and go the the link:
```http://127.0.0.1:8000/schema/```

##HTTP Errors
```400``` Invalid input

```404``` Object not found

```500``` Internal server error
