# Workout API

A RESTful API built with Flask that allows users to manage workouts and exercises.

## Project Description

Workout API is a RESTful API built with Flask that allows users to create, view, and delete workouts and exercises, as well as add exercises to workouts.

Each workout can contain multiple exercises. Workout exercises can store additional information such as reps, sets, and duration.

The application uses SQLite for the database, SQLAlchemy for database models and relationships, Flask-Migrate and Alembic for database migrations, and Marshmallow for serialization, deserialization, and schema validation.

## Features

- Create, view, and delete workouts
- Create, view, and delete exercises
- Add exercises to workouts
- Store reps, sets, and duration for workout exercises
- Database constraints
- Model-level validation
- Schema-level validation
- Database migrations
- Seed data for testing

## Technologies

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- SQLAlchemy
- Alembic

## Project Structure

```text
workout-api/
├── migrations/
├── server/
│   ├── app.py
│   ├── models.py
│   ├── schemas.py
│   └── seed.py
├── .gitignore
├── Pipfile
├── Pipfile.lock
└── README.md

Installation
1. Clone the Repository
git clone https://github.com/lynmora21/workout-api.git
cd workout-api

2. Install Dependencies
pipenv install

3. Activate the Virtual Environment
pipenv shell

4. Set the Flask Application

On macOS/Linux:

export FLASK_APP=server/app.py


On Windows PowerShell:

$env:FLASK_APP="server/app.py"

Database Setup
Initialize the Migration System

If the migration system has not already been initialized:

flask db init

Create a Migration

After making changes to the database models:

flask db migrate -m "create workout tables"

Apply Migrations
flask db upgrade

Seed the Database

Move into the server directory:

cd server


Run the seed file:

python seed.py


The seed file clears existing records and creates sample exercises, workouts, and workout-exercise records.

The seed file can be run multiple times without creating duplicate data.

Running the API

From the server directory, run:

python app.py


The API will be available at:

http://127.0.0.1:5555

API Endpoints
Workouts
GET /workouts

Returns a list of all workouts.

Example:

curl http://127.0.0.1:5555/workouts

GET /workouts/<id>

Returns a single workout, including its associated exercises and workout-exercise information.

Example:

curl http://127.0.0.1:5555/workouts/1

POST /workouts

Creates a new workout.

Example request body:

{
  "date": "2026-09-25",
  "duration_minutes": 45,
  "notes": "Upper body workout"
}


Example command:

curl -X POST http://127.0.0.1:5555/workouts \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-09-25","duration_minutes":45,"notes":"Upper body workout"}'

DELETE /workouts/<id>

Deletes a workout.

Example:

curl -X DELETE http://127.0.0.1:5555/workouts/1

Exercises
GET /exercises

Returns a list of all exercises.

Example:

curl http://127.0.0.1:5555/exercises

GET /exercises/<id>

Returns a single exercise and its associated workouts.

Example:

curl http://127.0.0.1:5555/exercises/1

POST /exercises

Creates a new exercise.

Example request body:

{
  "name": "Deadlift",
  "category": "Back",
  "equipment_needed": true
}


Example command:

curl -X POST http://127.0.0.1:5555/exercises \
  -H "Content-Type: application/json" \
  -d '{"name":"Deadlift","category":"Back","equipment_needed":true}'

DELETE /exercises/<id>

Deletes an exercise.

Example:

curl -X DELETE http://127.0.0.1:5555/exercises/1

Workout Exercises
POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises

Adds an exercise to a workout.

The request can include:

reps

sets

duration_seconds

Example request body:

{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 60
}


Example command:

curl -X POST http://127.0.0.1:5555/workouts/1/exercises/2/workout_exercises \
  -H "Content-Type: application/json" \
  -d '{"reps":10,"sets":3,"duration_seconds":60}'

Data Relationships

The application uses a join table called WorkoutExercise to connect workouts and exercises.

Workout
   |
   | has many
   v
WorkoutExercise
   |
   | belongs to
   v
Exercise


A workout can have many exercises through WorkoutExercise, and an exercise can belong to many workouts through WorkoutExercise.

The WorkoutExercise model stores additional information about an exercise within a specific workout:

Reps

Sets

Duration in seconds

Validation

The API performs validation at multiple levels to help maintain data integrity.

Database Constraints

Examples include:

Required fields cannot be NULL.

Exercise names must be unique.

The same exercise cannot be added to the same workout more than once.

Workout duration must be greater than zero.

Reps, sets, and duration must be greater than zero when provided.

Model Validations

Examples include:

Exercise names cannot be empty.

Exercise categories cannot be empty.

Workout duration must be greater than zero.

Workout dates cannot be in the future.

Reps and sets must be greater than zero.

Schema Validations

Marshmallow validates incoming request data.

Examples include:

Required fields must be provided.

Exercise names must contain at least two characters.

Exercise categories must contain at least two characters.

Workout duration must be at least one minute.

Reps must be at least one.

Sets must be at least one.

Duration in seconds must be at least one when provided.

Invalid data returns a 400 Bad Request response with validation error information.

HTTP Status Codes
Status Code	Meaning
200	Successful GET request
201	Resource successfully created
204	Resource successfully deleted
400	Validation or bad request error
404	Requested resource was not found
Author

Lyn Mora