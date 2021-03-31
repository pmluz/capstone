import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import traceback

from models import Actor, Movie, setup_db, db_drop_and_create_all
from auth import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # db_drop_and_create_all()

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    ## Routes for Actors
    '''
    GET /actors
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):  #payload
        try:
            selection = Actor.query.order_by(Actor.id).all()

            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in selection]
            }), 200

        except:
            abort(400)

    '''
    POST /actors
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(payload):
        body = request.get_json(force=True)
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        if not (new_name and new_age and new_gender):
            abort(422)

        try:
            new_actor = Actor(name=new_name, age=new_age, gender=new_gender)
            new_actor.insert()

            return jsonify({
                'success': True,
                'actors': [new_actor.format()]
            }), 200

        except Exception as e:
            print('Error while doing something:', e)
            traceback.print_exc()
            abort(401)

    '''
    PATCH /actors/<id>
        only Casting Director and Executive Producer can access this
    '''

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(422)

            body = request.get_json(force=True)
            new_name = body.get('name') if 'name' in body else actor.name
            new_age = body.get('age') if 'age' in body else actor.age
            new_gender = body.get(
                'gender') if 'gender' in body else actor.gender

            actor.name = new_name
            actor.age = new_age
            actor.gender = new_gender

            actor.update()

            return jsonify({'success': True, 'actors': [actor.format()]}), 200

        except Exception as e:
            print('Error while doing something:', e)
            traceback.print_exc()
            abort(401)

    '''
    DELETE /actors/<id>
        only with Executive Producer role can access this
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({'success': True, 'delete': id}), 200

        except:
            abort(401)

    ## Routes for Movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):  # payload
        try:
            selection = Movie.query.order_by(Movie.id).all()

            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in selection]
            }), 200

        except:
            abort(400)

    '''
    POST /movies
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):

        body = request.get_json(force=True)
        new_title = body.get('title')
        new_release_date = body.get('release_date')

        if not (new_title and new_release_date):
            abort(422)

        try:
            new_movie = Movie(title=new_title, release_date=new_release_date)
            new_movie.insert()

            return jsonify({
                'success': True,
                'movies': new_movie.format()
            }), 200

        except Exception as e:
            print('Error while doing something:', e)
            traceback.print_exc()
            abort(401)

    '''
    PATCH /movies/<id>
    '''

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            body = request.get_json(force=True)
            new_title = body.get('title') if 'title' in body else movie.title
            new_release_date = body.get(
                'release_date'
            ) if 'release_date' in body else movie.release_date

            movie.title = new_title
            movie.release_date = new_release_date

            movie.update()

            return jsonify({'success': True, 'movies': [movie.format()]})

        except Exception as e:
            print('Error while doing something:', e)
            traceback.print_exc()
            abort(401)

    '''
    DELETE /movies/<id>
        only with Executive Producer role can use this
    '''

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({'success': True, 'delete': id}), 200

        except:
            abort(401)

    @app.route('/', methods=['POST', 'GET'])
    def health():   
        return jsonify("Healthy")

    ## ERROR HANDLING
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(401)
    def unathorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unathorized'
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
