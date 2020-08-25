from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import db_setup, Movie, Actor
from flask_moment import Moment
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    db_setup(app)
    Moment(app)

    # Set up CORS. Allow '*' for origins.

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/movies')
    @requires_auth('get:movies')
    def retrieve_movies(jwt):
        # handle GET requests for all available movies.
        movies_query = Movie.query.all()
        movies = []
        count = 0
        data = {}
        for value in movies_query:
            data[count] = {'title': value.title,
                           'release_date': value.release_date}
            movies.append(data[count])
            count += 1
        return jsonify({
            'success': True,
            'movies': movies
        })

    @app.route('/actors')
    @requires_auth('get:actors')
    def retrieve_actors(jwt):
        # handle GET requests for all available actors.
        actors_query = Actor.query.all()
        actors = []
        count = 0
        data = {}
        for value in actors_query:
            data[count] = {'name': value.name,
                           'age': value.age, 'gender': value.gender}
            actors.append(data[count])
            count += 1
        return jsonify({
            'success': True,
            'actors': actors
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(jwt):
        body = request.get_json()
        try:
            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)

            # Create a new movie
            movie = Movie(title=new_title, release_date=new_release_date)
            # Insert a new movie
            movie.insert()
            data = []
            data.append(
                {'title': movie.title, 'release_date': movie.release_date})
            # Return data results
            return jsonify({
                'success': True,
                'movie': data
            })
        except Exception as error:
            raise error

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwt):
        body = request.get_json()
        try:
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)

            # Create a new actor
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            # Insert a new actor
            actor.insert()
            data = []
            data.append({'name': actor.name, 'age': actor.age,
                         'gender': actor.gender})
            # Return data results
            return jsonify({
                'success': True,
                'movie': data
            })
        except Exception as error:
            raise error

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, id):
        body = request.get_json()
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            # abort 404 if there is no movie found
            if movie is None:
                abort(404)
            # update a single movie
            if 'title' in body and 'release_date' in body:
                movie.title = body.get('title')
                movie.release_date = body.get('release_date')
                movie.update()
            data = []
            data.append(
                {'title': movie.title, 'release_date': movie.release_date})
            return jsonify({'success': True, 'movies': data})
        except Exception as error:
            raise error

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, id):
        body = request.get_json()
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            # abort 404 if there is no actor found
            if actor is None:
                abort(404)
            # update a single actor
            if 'name' in body and 'age' in body and 'gender':
                actor.name = body.get('name')
                actor.age = body.get('age')
                actor.gender = body.get('gender')
                actor.update()
            data = []
            data.append({'name': actor.name, 'age': actor.age,
                         'gender': actor.gender})
            return jsonify({'success': True, 'actors': data})
        except Exception as error:
            raise error

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, id):
        try:
            # Get a movie by id
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            # abort 404 if there is no movie found
            if movie is None:
                abort(404)
            movie.delete()
            # Return data results
            return jsonify({
                'success': True,
                'delete':  movie.id
            })
        except Exception as error:
            raise error

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, id):
        try:
            # Get an actor by id
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            # abort 404 if there is no actor found
            if actor is None:
                abort(404)
            actor.delete()
            # Return data results
            return jsonify({
                'success': True,
                'delete':  actor.id
            })
        except Exception as error:
            raise error

    # error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(422)
    def unprocrssable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocrssable"
        }), 422

    @app.errorhandler(500)
    def internal_Server_rror(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "METHOD NOT ALLOWED"
        }), 405

    '''
    implement error handler for AuthError error handler
    '''
    @app.errorhandler(AuthError)
    def authentication_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error
            }), error.status_code

    return app
