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
        self.casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc1MjM0MDk4MjMwNzc4NjMzOTUiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNjYyMDgsImV4cCI6MTYxNzI1MjYwOCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.lPUhEIqA5Dkpi-hk32aUSmopWihKVOjUr6buwOvU3dO5XFX39Htddy0S41GG4bI5zvXdD8H2XASCfK7VAoeoOBlmO5jLMqo1LmZ3YvQGdYnF4r5xVYuEMgeuNX0XS6qBdGD39YLZKQEqT6oEmfT9SCRriDA0rLpeGb4LkLVOF1Wrr07espTJI4T9xSVr6Qk5wj3qXmjipCVXVR6XqMOmBu07Yw-yXQRJzQVtmzm-PiHA2BhIlpXPUjBcdwSPbAb2cjdPrMCgOBuCEFy-bOc0NUfNY2RNSLQbIjxX3BRHk154rhgwcYm8quuZlsGKcRPiBBXaCK_1ae4209kpiWrlhA'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDY2NTk5Nzg3MDUyNTY4MjcxMzkiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNzA0NjUsImV4cCI6MTYxNzI1Njg2NSwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.T2_asmI0ZoS7L9Xh1X6CS_kWuBfaVeDJvR9QNEaiharI2Fx0b85b9yqeGYIhAADtdklWPISfN-y6GtK8J4Vcqdu4eMg5wDWgDCGEhH6ww09OHOai075q5NCxGqSaMBt0Cc1RUUswONKifejsJKG69dimdZo3tZqpVkJLrWD6LDKID6VrPOdyRj_HBzDmvnUfadokM33GP27i-BjWH9XQXFn73llMGPKOxFxHtmac-zvvugCE7ARnywSvKcSJQDVCRg2abxPFPi9sfqrUA6nmHWEwQItPQ3D8fbfOvtOfRm1HO0jfANR81EunXsp-QVjC9cwsyM3IiJqQhj0RVCDnkw'
        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNzA1MTcsImV4cCI6MTYxNzI1NjkxNywiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Cy0gXkEK4rZGuuFapPi-P2vtbHiMvIryyvuHptTvbXhQCpnl3pAJNlx74greyJrlGUL46pakJUcVTeGpo-Oxm8zS0ybbLr2uxWmfnS8iWN8C7Hz8533GJuvGnUNEVpxalxSO6aoXk68q9Y4Mq8lvVXea17wWlB0JZ4gNUSKxCCtgQCq2Lshj9_43E2VGGYChjyK2H_3SHV2c78luB-ptATL1uD6KVq6BN409dcmEBgyncRdtFYDsbc1gEM7S8Kwbxnfkob0k8exu-v0UN0kXuigHpZadCy_K5VNQ9QaO8uK5Bd2a5NfGm9tAGC6GaSetamoyAWVmiKKQWwx3FXeUHg'

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