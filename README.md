## Full Stacka Nano - Capstone Project

## Getting Started

### Installing Dependencies

1. Create aand activate virtualenv:

   ```jsx
   cd YOUR_PROJECT_PATH_DIRECTORY
   python3 -m venv env
   source env/bin/activate
   ```

2. Install dependencies:

   ```jsx
   pip install -r requirements.txt
   ```

## Running the server

1. From within the `./src` directory first ensure you are working using your created virtual environment.
2. To run the application, run the following commands:

   ```jsx
       export FLASK_APP=app.py
       flask run --reload
   ```

## API Reference

### Getting Started

1. Base URL: This app can only run locally. The backend app is hosted at default, http://127.0.0.1:5000/, which is set as a proxy in the frontend conifguration.
2. Authentication: This version of the application does requires authentication.

### Error Handling

Errors are returned as JSON objects in the following format:

```jsx
{
    'success': False,
    'error': 400,
    'message': 'bad request'
}
```

The API will return four error types when requests fail:

- 400: Bad Request
- 401: Unathorized
- 404: Resource Not Found
- 422: Unprocessable

### Endpoints for Actors

**GET /actors**

- General:
  - Returns list of actors
- Sample: `curl http://127.0.0.1:5000/actors`

  ```jsx
  {
      "actors": [
          {
              "age":53,
              "gender":"male",
              "id":2,
              "name":"Julia Roberts"
          },
          {
              "age":71,
              "gender":"male",
              "id":3,
              "name":"Richard Gere"
          },
          {
              "age":32,
              "gender":"female",
              "id":4,
              "name":"Awkwafina"
          },
          {
              "age":37,
              "gender":"male",
              "id":5,
              "name":"Donald Glover"
          }
      ],
      "success": true
  }
  ```

**POST /actors**

- General:
  - Creates a new actor using the submitted name, age, and gender.
  - Returns the id of the created actor and success value.
- Sample: `curl -X POST -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" -d '{"name": "Tom Hanks", "age": "64", "gender": "female"}' http://127.0.0.1:5000/actors`

  ```jsx
  {
      "actors":
      {
          "age": 64,
          "gender": "female",
          "id": 6,
          "name": "Tom Hanks"
      },
      "success": true
  }
  ```

**PATCH /actors/int:id**

- General:

  - Updates actor information based on the given ID.
  - Returns id, name, age, gender, and success value.

- Sample: `curl -X PATCH -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" -d '{"gender": "male"}' http://127.0.0.1:5000/actors/<id>`

  ```jsx
  {
      "actors":
      {
          "age": 64,
          "gender": "male",
          "id": 1,
          "name": "Tom Hanks"
      },
      "success": true
  }
  ```

**DELETE /actors/int:id**

- General:
  - Deletes the actor of the given ID if it exists.
  - Returns the id of the deleted actor and success value.
- Sample:
  `curl -X DELETE -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" http://127.0.0.1:5000/actors/1`

  ```jsx
  {
      "delete": 1,
      "success": true
  }
  ```

### Endpoints for Movies

**GET /movies**

- General:
  - Returns list of movies.
- Sample: `curl http://127.0.0.1:5000/movies`

  ```jsx
  {
      "movies": [
          {
              "id":2,
              "release_date":"2012",
              "title":"The Hobbit: An Unexpected Journey"
          },
          {
              "id":3,
              "release_date":"2013",
              "title":"The Hobbit: The Desolation of Smaug"
          },
          {
              "id":4,
              "release_date":"1999",
              "title":"Runaway Bride"
          }
      ],
      "success":true
  }
  ```

**POST /movies**

- General:

  - Creates a new movie using submitted title and release date.
  - Returns id, title, release date and success value.

- Sample:
  `curl -X POST -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" -d '{"title": "ET", "release_date": "2000"}' http://127.0.0.1:5000/movies`

      ```jsx
      {
          "movies":
          {
              "id": 5,
              "release_date": "2000",
              "title": "ET"
          },
          "success": true
      }
      ```

**PATCH /movies/int:id**

- General:
  - Updates movie information based on the given ID.
  - Returns id, release_date, title, and success value.
- Sample:
  `curl -X PATCH -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" -d '{"release_date": "1982"}' http://127.0.0.1:5000/movies/5`

  ```jsx
  {
      "movies":
      {
          "id": 5,
          "release_date": "1982",
          "title": "ET"
      },
      "success": true
  }
  ```

**DELETE /movies/int:id**

- General:
  - Deletes the movie of the given ID if it exists.
  - Returns the id of the deleted movie and success value.
- Sample:
  `curl -X DELETE -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTY2Mzc0MTAsImV4cCI6MTYxNjcyMzgxMCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Zxn1KvzQ-A-6fPDhx9Evt0N4GazkkHuFJtC4V0nJQ1B4w70MdCfyZ_39KAI35N1VfB1NSpmw3WYirX0E8uE1UcfluzsYozFzEfUrdcqf9lNBbaDW88VGy3AGKD9bVfgFwJAq-iMHn40B_ogOoi8xgeZRGX1BP-p-6-3rXze9nGiOtaEz3ZT8CIAuUGnWw8PRjZQkBnVmkLuVnukMFbl-_XFxoedC9Fysq4J0-JbxUrVCF3mI9-zBolZl30Tb0G0DqMkcaP8KnXzGPAiQGC5fUSWk64lq2onvEGu9DcrQ9mgil8drFOw9sG1Vnp0IbgCpzmKDUP-qAHKpbVGaXwSnbQ" http://127.0.0.1:5000/movies/1`

  ```jsx
  {
      "delete": 1,
      "success": true
  }
  ```

### Role Based Accessed Controls (Permissions)

- **Casting Assistant**
  - GET /actors
  - Get /movies
- **Casting Director**
  - GET /actors
  - POST /actors
  - PATCH /actors/id
  - DELETE /actors/id
  - GET /movies
  - PATCH /movies/id
- **Executive Producer**
  - GET /actors
  - POST /actors
  - PATCH /actors/id
  - DELETE /actors/id
  - GET /movies
  - POST /movies
  - PATCH /movies/id
  - DELETE /movies/id

### Authentication

**Casting Assistant**
```jsx
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc1MjM0MDk4MjMwNzc4NjMzOTUiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNjYyMDgsImV4cCI6MTYxNzI1MjYwOCwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.lPUhEIqA5Dkpi-hk32aUSmopWihKVOjUr6buwOvU3dO5XFX39Htddy0S41GG4bI5zvXdD8H2XASCfK7VAoeoOBlmO5jLMqo1LmZ3YvQGdYnF4r5xVYuEMgeuNX0XS6qBdGD39YLZKQEqT6oEmfT9SCRriDA0rLpeGb4LkLVOF1Wrr07espTJI4T9xSVr6Qk5wj3qXmjipCVXVR6XqMOmBu07Yw-yXQRJzQVtmzm-PiHA2BhIlpXPUjBcdwSPbAb2cjdPrMCgOBuCEFy-bOc0NUfNY2RNSLQbIjxX3BRHk154rhgwcYm8quuZlsGKcRPiBBXaCK_1ae4209kpiWrlhA
```
**Casting Director**
```jsx
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDY2NTk5Nzg3MDUyNTY4MjcxMzkiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNzA0NjUsImV4cCI6MTYxNzI1Njg2NSwiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.T2_asmI0ZoS7L9Xh1X6CS_kWuBfaVeDJvR9QNEaiharI2Fx0b85b9yqeGYIhAADtdklWPISfN-y6GtK8J4Vcqdu4eMg5wDWgDCGEhH6ww09OHOai075q5NCxGqSaMBt0Cc1RUUswONKifejsJKG69dimdZo3tZqpVkJLrWD6LDKID6VrPOdyRj_HBzDmvnUfadokM33GP27i-BjWH9XQXFn73llMGPKOxFxHtmac-zvvugCE7ARnywSvKcSJQDVCRg2abxPFPi9sfqrUA6nmHWEwQItPQ3D8fbfOvtOfRm1HO0jfANR81EunXsp-QVjC9cwsyM3IiJqQhj0RVCDnkw
```
**Executive Producer**
```jsx
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZaUUVGenM4RDJRZnp4SDF5S3lmOCJ9.eyJpc3MiOiJodHRwczovL3UtZnNuZC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDM3Mzc0NzYxNjYyNDA3NjcxMjMiLCJhdWQiOlsiY2FzdGluZ2FnZW5jeSIsImh0dHBzOi8vdS1mc25kLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTcxNzA1MTcsImV4cCI6MTYxNzI1NjkxNywiYXpwIjoiZXRMUnhhQjZaUk12ZkNvR1FicHRMUDZRTzMySnNKdTUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Cy0gXkEK4rZGuuFapPi-P2vtbHiMvIryyvuHptTvbXhQCpnl3pAJNlx74greyJrlGUL46pakJUcVTeGpo-Oxm8zS0ybbLr2uxWmfnS8iWN8C7Hz8533GJuvGnUNEVpxalxSO6aoXk68q9Y4Mq8lvVXea17wWlB0JZ4gNUSKxCCtgQCq2Lshj9_43E2VGGYChjyK2H_3SHV2c78luB-ptATL1uD6KVq6BN409dcmEBgyncRdtFYDsbc1gEM7S8Kwbxnfkob0k8exu-v0UN0kXuigHpZadCy_K5VNQ9QaO8uK5Bd2a5NfGm9tAGC6GaSetamoyAWVmiKKQWwx3FXeUHg
```
## Website
https://castingagency-app.herokuapp.com/
