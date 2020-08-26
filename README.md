# capstone project for the udacity full stack nanodegree program.

Heroku link: ``` https://my-capstone-app.herokuapp.com/ ```

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

# Motivation

* Architect relational database models in Python.
* Utilize SQLAlchemy to conduct database queries.
* Follow RESTful principles of API development.
* Structure endpoints to respond to four HTTP methods, including error handling.
* Implement authentication and Role Based Access Control using Auth0.
* Enable Role-Based Authentication and role-based access control (RBAC) in a Flask application.
* Deploy the app to Heroku.


## Installing Dependencies
 
##### Python 3.7

Follow instructions to install the latest version of python for your platform in the python docs ``` https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ ```

##### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

``` 
pip install -r requirements.txt 
```

This will install all of the required packages we selected within the requirements.txt file.

##### Key Dependencies

* Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

* SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.


# Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
export DATABASE_URL=<database-url>
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

```

# API Reference

# Getting Started

Base URL: This application can be run locally. The hosted version is at ``` https://my-capstone-app.herokuapp.com. ```

Authentication: This application requires authentication to perform various actions. All the endpoints require various permissions using Auth0's Role Based Access Control (RBAC).

The application has three different types of roles:

viewer
only has view the list of actors and movies permissions.
* get:actors
* get:movies 
Manager
has all permissions to make all actions
* get:actors
* get:movies
* patch:actors
* patch:movies
* post:movies
* post:actors
* delete:movies
* delete: actors
# Error Handling

Errors are returned as JSON in the following format:

```
{
  "error": 404, 
  "message": "Not Found", 
  "success": false
}
```
The API will return five types of errors:

* 400 - bad request
* 404 - resource not found
* 422 - unprocessable
* 500 - internal server error
* 405 - method not allowed
* 401 - Unauthorized
* 403 - Forbidden

# Endpoints

##### GET /movies

General:

* Returns a list of movies.
* sample: curl https://my-capstone-app.herokuapp.com/movies. 

```
{
  "movies": [
    {
      "release_date": "December 10, 2009",
      "title": "Avatar"
    },
    {
      "release_date": "April 22, 2019",
      "title": "Avengers: Endgame"
    },
    {
      "release_date": "November 18, 1997",
      "title": "Titanic"
    },
    {
      "release_date": "December 14, 2015",
      "title": "Star Wars: The Force Awakens"
    },
    {
      "release_date": "April 23, 2018",
      "title": "Avengers: Infinity War"
    },
    {
      "release_date": "May 29, 2015",
      "title": "Jurassic World"
    },
    {
      "release_date": "March 26, 2015",
      "title": "Furious 7"
    }
  ],
  "success": true
}
```
##### GET /actors

General:

* Returns a list of actors.
* sample: curl https://my-capstone-app.herokuapp.com/actors. 

```
{
  "actors": [
    {
      "age": "37 years",
      "gender": "male",
      "name": "Chris Hemsworth"
    },
    {
      "age": "45 years",
      "gender": "male",
      "name": "Bradley Cooper"
    },
    {
      "age": "56 years",
      "gender": "male",
      "name": "Brad Pitt"
    },
    {
      "age": "49 years",
      "gender": "male",
      "name": "Matt Damon"
    },
    {
      "age": "51 years",
      "gender": "male",
      "name": "Will Smith"
    },
    {
      "age": "45 years",
      "gender": "male",
      "name": "Leonardo DiCaprio"
    },
    {
      "age": "48 years",
      "gender": "male",
      "name": "Dwayne Johnson"
    }
  ],
  "success": true
}
```
##### POST /movies

General:

If create new movie:

* Returns the title of the created movie, success value and release date.
* sample: curl -X POST -H "Content-Type: application/json" -d "{ \"title\": \"Goodfellas\",  \"release_date\": \"September 9, 1990\"}" https://my-capstone-app.herokuapp.com/movies

```
{
  "movie": [
    {
      "release_date": "September 9, 1990",
      "title": "Goodfellas"
    }
  ],
  "success": true
}
```

##### POST /actors

General:

If create new actor:

* Returns the name of the created actors, success value, age and gender.
* sample: curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Ray Liotta\",  \"age\": \"65 years\", \"gender\": \"male\"}" https://my-capstone-app.herokuapp.com/actors

```
{
  "movie": [
    {
      "age": "65 years",
      "gender": "male",
      "name": "Ray Liotta"
    }
  ],
  "success": true
}
```
##### PATCH /movies

General:

If update exit movie:

* Returns the title of the updated movie, success value and release date.
* sample: curl -X  PATCH -H "Content-Type: application/json" -d "{\"title\": \"Goodfellas\",  \"release_date\": \"September 10, 1990\"}"https://my-capstone-app.herokuapp.com/movies/10

```
{
  "movies": [
    {
      "release_date": "September 10, 1990",
      "title": "Goodfellas"
    }
  ],
  "success": true
}
```
##### PATCH /actors

General:

If update exit actor:

* Returns the name of the updated actor, success value, age and gender.
* sample: curl -X  PATCH -H "Content-Type: application/json" -d "{\"name\": \"Bradley Cooper\",  \"age\": \"46 years\", \"gender\": \"male\"}" https://my-capstone-app.herokuapp.com/actors/2

```
{
  "actors": [
    {
      "age": "46 years",
      "gender": "male",
      "name": "Bradley Cooper"
    }
  ],
  "success": true
}
```

##### DELETE /movies/{id}

General:

* Deletes the movie of the given ID if it exists. 
* Returns the id of the deleted movie and success value.
* curl -X DELETE https://my-capstone-app.herokuapp.com/movies/8

```
{
  "delete": 8,
  "success": true
}
```
##### DELETE /actors/{id}

General:

* Deletes the actor of the given ID if it exists. 
* Returns the id of the deleted actor and success value.
* curl -X DELETE https://my-capstone-app.herokuapp.com/actors/6

```
{
  "delete": 6,
  "success": true
}
```
# Testing
For testing the backend, run the following commands (in the exact order):

```
dropdb -U postgres agency_test
Password: 5678.mna
createdb -U postgres agency_test
Password: 5678.mna
psql agency_test postgres < agency.psql
Password for user postgres: 5678.mna
python test_app.py
```
The first time you run the tests, omit the dropdb command.
 
