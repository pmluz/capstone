import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Movie, Actor, setup_db


class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgresl://{}/{}".format(
            'localhost:5432', self.database_name)
        # setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # tokens for all roles
        self.casting_assistant_token = os.environ.get('CASTING_ASSISTANT_TOKEN')
        self.casting_director_token = os.environ.get('CASTING_DIRECTOR_TOKEN')
        self.executive_producer_token = os.environ.get('EXECUTIVE_PRODUCER_TOKEN')

        # sample data
        self.new_movie = {'title': 'Minari', 'release_date': '2021'}

        self.new_actor = {
            'name': 'Richard Gere',
            'age': '71',
            'gender': 'male'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Tests for Casting Assistant: /actors
    '''

    def test_casting_assistant_get_actors(self):
        res = self.client().get('/actors',
                                headers={
                                    'Authorization':
                                    'Bearer ' + self.casting_assistant_token
                                })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_assistant_cannot_create_new_actor(self):
        res = self.client().post('/actors',
                                 json=self.new_actor,
                                 headers={
                                     'Authorization':
                                     'Bearer ' + self.casting_assistant_token
                                 })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')
    '''
    Tests for Casting Assistant: /movies
    '''

    def test_casting_assistant_get_movies(self):
        res = self.client().get('/movies',
                                headers={
                                    'Authorization':
                                    'Bearer ' + self.casting_assistant_token
                                })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_assistant_cannot_create_new_movie(self):
        res = self.client().post('/movies',
                                 json=self.new_movie,
                                 headers={
                                     'Authorization':
                                     'Bearer ' + self.casting_assistant_token
                                 })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')
    '''
    Tests for Casting Director: /actors
    '''

    def test_casting_director_get_actors(self):
        res = self.client().get(
            '/actors',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    '''
    Works!
    '''

    def test_casting_director_create_new_actor(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_casting_director_update_actor(self):
        res = self.client().patch(
            '/actors/3',
            json={'gender': 'male'},
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['gender'], 'male')

    def test_casting_director_update_actor_failed_missing_header(self):
        res = self.client().patch(
            '/actors/100')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is missing.')
    
    # '''
    # Tests for Casting Director: /movies
    # '''

    def test_casting_director_get_movies(self):
        res = self.client().get(
            '/movies',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_casting_director_cannot_create_movie(self):
        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_casting_director_cannot_delete_movie(self):
        res = self.client().delete(
            '/movies/1',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_casting_director_update_movie(self):
        id = 2
        release_date = '0000'
        res = self.client().patch(
            '/movies/' + str(id),
            json={'release_date': release_date},
            headers={'Authorization': 'Bearer ' + self.casting_director_token})

        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id ==  id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['release_date'], release_date)

    def test_casting_director_update_movie_failed_missing_header(self):
        res = self.client().patch(
            '/movies/100')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is missing.')

    # '''
    # Tests for Executive Producer: /actors
    # '''

    def test_executive_producer_get_actors(self):
        res = self.client().get('/actors',
                                headers={
                                    'Authorization':
                                    'Bearer ' + self.executive_producer_token
                                })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_executive_producer_delete_actor(self):
        actor = Actor(name="Dummy name", age=0, gender="other")
        actor.insert()

        res = self.client().delete('/actors/' + str(actor.id),
                                   headers={
                                       'Authorization':
                                       'Bearer ' +
                                       self.executive_producer_token
                                   })
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == actor.id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertEqual(data['delete'], actor.id)
        self.assertEqual(actor, None)
    


    def test_executive_producer_update_actor(self):
        res = self.client().patch('/actors/3',
                                  json={'gender': 'female'},
                                  headers={
                                      'Authorization':
                                      'Bearer ' + self.executive_producer_token
                                  })
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['gender'], 'female')

    # '''
    # Tests for Executive Producer: /movies
    # '''

    def test_executive_producer_get_movies(self):
        res = self.client().get('/movies',
                                headers={
                                    'Authorization':
                                    'Bearer ' + self.executive_producer_token
                                })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_executive_producer_create_new_movie(self):
        res = self.client().post('/movies',
                                 json=self.new_movie,
                                 headers={
                                     'Authorization':
                                     'Bearer ' + self.executive_producer_token
                                 })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_executive_producer_delete_movie(self):
        movie = Movie(title="Dummy movie", release_date="0000")
        movie.insert()

        res = self.client().delete('/movies/' + str(movie.id),
                                   headers={
                                       'Authorization':
                                       'Bearer ' +
                                       self.executive_producer_token
                                   })
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == movie.id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertEqual(data['delete'], movie.id)
        self.assertEqual(movie, None)

    

    

    '''
    Updates the db but test keeps failing for some reason
    '''

    def test_executive_producer_update_movie(self):
        release_date = '1982'
        res = self.client().patch('/movies/2',
                                  json={'release_date': release_date},
                                  headers={
                                      'Authorization':
                                      'Bearer ' + self.executive_producer_token
                                  })
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['release_date'], release_date)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()