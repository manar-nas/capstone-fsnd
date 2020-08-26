import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from functools import wraps
from models import db_setup, Movie, Actor
from flask import abort
from unittest.mock import patch

''' Check endpoints without having to pass the
system authentication. '''


def mock_decorator(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = 'token'
            try:
                payload = 'token'
            except Exception:
                abort(401)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator


patch('app.requires_auth', mock_decorator).start()


class AgencyTestCase(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', '5678.mna', 'localhost:5432', self.database_name)
        db_setup(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            "title": "Fight Club",
            "release_date": "September 10, 1999"
        }

        self.new_actor = {
            "name": "Sarah Gadon",
            "age": "33 years",
            "gender": "female"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # test for get movies

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_405_get_movie(self):
        res = self.client().get('/movies/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'METHOD NOT ALLOWED')

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_405_get_actor(self):
        res = self.client().get('/movies/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'METHOD NOT ALLOWED')

    # test for post

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_405_if_movie_creation_fails(self):
        res = self.client().post('/movies/100', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'METHOD NOT ALLOWED')

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_405_if_actor_creation_fails(self):
        res = self.client().post('/actors/100', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'METHOD NOT ALLOWED')

    # test for update one movie

    def test_update_movie(self):
        res = self.client().patch(
            '/movies/1', json={"release_date": "December 11, 2009"})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['release_date'], "December 10, 2009")

    def test_for_failed_update_movie(self):
        res = self.client().patch('/movies/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    # test for update one actor
    def test_update_actor(self):
        res = self.client().patch('/actors/1', json={'age': "38 years"})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['age'], "37 years")

    def test_failed_update_actor(self):
        res = self.client().patch('/actors/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    # test for delete one movie
    def test_movie_delete(self):
        res = self.client().delete('/movies/8')
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 8).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie, None)

    def test_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    # test for delete one actor
    def test_actor_delete(self):
        res = self.client().delete('/actors/7')
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 7).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor, None)

    def test_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
