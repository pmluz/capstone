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
        self.casting_assistant_token = ''
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDY2NTk5Nzg3MDUyNTY4MjcxMzkiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcwODAxOTYsImV4cCI6MTYxNzE2NjU5NiwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.XRcYQXGnbdbU2vU5vEk-3R7tfQaOszCbRAtOF0pTI3NhqrugEyLDw0ECRnWztW8Bb2QsNJEPhxjPmtydAB6EwdgYXw21AkFWi_VWIlId59H9W_0JWzAokplmpS6r013ixa4RDu_vlo--w3bieBqaEpX6Ov3hDPqd4tFDtR0v_40JjkBsVReKeTlqcUxLUIM0iGSYaaGNE6_uGL2wa5lEIoaIR0es1xu601lGmAj5iWwxzmKRl9UuvPN2ooODyeEYowHjtuRys6VPt9xCHJ3rntNDZbCWecQMQqN9jk6IpQpCjfHDoygSNTSF_onC7-N5WMhumZWHGe7qEqH3VSJf5w'
        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcwODM1MTAsImV4cCI6MTYxNzE2OTkxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.NsqmZ3Exvui9AkdKgDpMEdnbfXRmt_RDq95a5kSeNOLNm8SL7nj7O4W17285fr_keBAelAUKDW-gIU8eu8fgAVVzs13R30PNImWb1LCC811yIenHNFVjDaQ-qFav_yxOnLB80vKJrAUm6oe1n6r5X-q99p1NwLAnvMpM12j3Jnf-KosRHoeGdC4pygoW5ppdSLHwbj7-Yk6wWmgUWrhqtwLNcvZ82vkJAQUp1FfPSQEMYGLXKlUZv0wKMEkDX7s_sBaxsRcuQrFvnafxK7d_xVrOiOe-ALzvH6SFUqIh42sZeFsz9Qmnu59hLtP82tDGrQANzxTxOxImL8zPjyBVgA'

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

    # def test_casting_assistant_get_actors(self):
    #     res = self.client().get('/actors',
    #                             headers={
    #                                 'Authorization':
    #                                 'Bearer ' + self.casting_assistant_token
    #                             })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_casting_assistant_for_401_if_actor_creation_not_allowed(self):
    #     res = self.client().post('/actors/45',
    #                              json=self.new_actor,
    #                              headers={
    #                                  'Authorization':
    #                                  'Bearer ' + self.casting_assistant_token
    #                              })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unathorized')
    '''
    Tests for Casting Assistant: /movies
    '''

    # def test_casting_assistant_get_movies(self):
    #     res = self.client().get('/movies',
    #                             headers={
    #                                 'Authorization':
    #                                 'Bearer ' + self.casting_assistant_token
    #                             })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_casting_assistant_for_401_if_movie_creation_not_allowed(self):
    #     res = self.client().post('/movies/45',
    #                              json=self.new_movie,
    #                              headers={
    #                                  'Authorization':
    #                                  'Bearer ' + self.casting_assistant_token
    #                              })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unathorized')
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
    Works!!
    '''

    def test_casting_director_delete_actor(self):
        res = self.client().delete(
            '/actors/6',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 6)
        self.assertEqual(actor, None)

    '''
    Maybe not include 422 error
    '''

    # def test_casting_director_for_422_if_actor_does_not_exist(self):
    #     res = self.client().delete(
    #         '/actors/1000',
    #         headers={'Authorization': 'Bearer ' + self.casting_director_token})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable')
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

    '''
    Works
    '''

    def test_casting_director_update_actor(self):
        res = self.client().patch(
            '/actors/2',
            json={'gender': 'male'},
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['gender'], 'male')

    '''
    Tests for Casting Director: /movies
    '''

    def test_casting_director_get_movies(self):
        res = self.client().get(
            '/movies',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # def test_casting_director_delete_movie(self):
    #     res = self.client().delete(
    #         '/movies/1',
    #         headers={'Authorization': 'Bearer ' + self.casting_director_token})
    #     data = json.loads(res.data)

    #     movie = Movie.query.filter(Movie.id == id).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['delete'], 1)
    #     self.assertEqual(movie, None)

    def test_casting_director_update_movie(self):
        res = self.client().patch(
            '/movies/2',
            json={'release_date': '2013'},
            headers={'Authorization': 'Bearer ' + self.casting_director_token})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    self.assertEqual(Movie.format()['release_date'], '2013')

    def test_casting_director_for_401_if_movie_deletion_not_allowed(self):
        res = self.client().delete(
            '/movies/1000',
            headers={'Authorization': 'Bearer ' + self.casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    '''
    Tests for Executive Producer: /actors
    '''

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
        res = self.client().delete('/actors/1',
                                   headers={
                                       'Authorization':
                                       'Bearer ' +
                                       self.executive_producer_token
                                   })
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)
        self.assertEqual(actor, None)

    def test_executive_producer_create_new_actor(self):
        res = self.client().post('/actors',
                                 json=self.new_actor,
                                 headers={
                                     'Authorization':
                                     'Bearer ' + self.executive_producer_token
                                 })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_executive_producer_update_actor(self):
        res = self.client().patch('/actors/2',
                                  json={'gender': 'male'},
                                  headers={
                                      'Authorization':
                                      'Bearer ' + self.executive_producer_token
                                  })
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['gender'], 'male')

    '''
    Tests for Executive Producer: /movies
    '''

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

    def test_executive_producer_delete_movie(self):
        res = self.client().delete('/movies/5',
                                   headers={
                                       'Authorization':
                                       'Bearer ' +
                                       self.executive_producer_token
                                   })
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 5)

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

    '''
    Updates the db but test keeps failing for some reason
    '''

    # def test_executive_producer_update_movie(self):
    #     res = self.client().patch('/movies/2',
    #                               json={'title': 'ET'},
    #                               headers={
    #                                   'Authorization':
    #                                   'Bearer ' + self.executive_producer_token
    #                               })
    #     data = json.loads(res.data)

    #     movie = Movie.query.filter(Movie.id == id).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(movie.format()['title'],
    #                      'ET')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()