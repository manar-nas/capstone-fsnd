# Motivation
This is my capstone project submission for the Udacity Full-Stack Developer Nanodegree program.

The goal is to demonstrate the ability to:

* Design data models and their relations using SQLAlchemy.
* Write database queries using SQLAlchemy.
* Design an HTTP API with Flask.
* Document the API and development guide in detail.
* Implement authentication and Role Based Access Control using Auth0.
* Test the API and access control capabilities. 
* Deploy the app to Heroku.

Once you have your virtual environment setup and running, install dependencies by naviging to the /starter directory and running:

```
pip install -r requirements.txt
``` 
To run the application run the following commands:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run 
```
Flask documentation. the application is run on
```
http://127.0.0.1:5000/
```

# Tests
In order to run tests navigate to the backend folder and run the following commands:

```
dropdb agency_test 
createdb agency_test
psql agency_test < agency.psql
python test_app.py
```
The first time you run the tests, omit the dropdb command.


## API Reference befor authentication
## Getting Started

* Base URL: At presnt this app can only be run locally and is not hosted as a base URL. The backend app is hosted at default, ```http://127.0.0.1:5000/```, which is set as a proxy in the frontend configuration.
* Authentication: For test using a Postman collection with access tokens is provided for convenience (agency-postman-collection.postman_collection.json).

#### Error Handling

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

##### GET /movies

General:

* Returns a list of movies.
* sample: curl http://127.0.0.1:5000/movies. 

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
* sample: curl http://127.0.0.1:5000/actors. 

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
* sample: curl -X POST -H "Content-Type: application/json" -d "{ \"title\": \"Goodfellas\",  \"release_date\": \"September 9, 1990\"}" http://127.0.0.1:5000/movies

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
* sample: curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Ray Liotta\",  \"age\": \"65 years\", \"gender\": \"male\"}" http://127.0.0.1:5000/actors

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
* sample: curl -X  PATCH -H "Content-Type: application/json" -d "{\"title\": \"Goodfellas\",  \"release_date\": \"September 10, 1990\"}" http://127.0.0.1:5000/movies/10

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
* sample: curl -X  PATCH -H "Content-Type: application/json" -d "{\"name\": \"Bradley Cooper\",  \"age\": \"46 years\", \"gender\": \"male\"}" http://127.0.0.1:5000/actors/2

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
* curl -X DELETE http://127.0.0.1:5000/movies/8

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
* curl -X DELETE http://127.0.0.1:5000/actors/6

```
{
  "delete": 6,
  "success": true
}
```
## Authentication and Permissions
#### Authentication is handled via Auth0.

###### API endpoints use these permissions:

* 'delete:actors'
* 'delete:movies'
* 'patch:actors'
* 'patch:movies'
* 'post:movies'
* 'post:actors'
* 'get:actors'
* 'get:movies'

 
