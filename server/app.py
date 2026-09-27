from flask import Flask, request
from flask_migrate import Migrate

from models import db, Workout, Exercise, WorkoutExercise
from schemas import (
    WorkoutSchema,
    WorkoutDetailSchema,
    ExerciseSchema,
    ExerciseDetailSchema,
    WorkoutExerciseSchema
)


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_detail_schema = WorkoutDetailSchema()

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

exercise_detail_schema = ExerciseDetailSchema()

workout_exercise_schema = WorkoutExerciseSchema()


@app.route("/")
def home():
    return {"message": "Workout API is running!"}


# -------------------------
# WORKOUT ROUTES
# -------------------------

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return workouts_schema.dump(workouts), 200


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return {"error": "Workout not found"}, 404

    return workout_detail_schema.dump(workout), 200


@app.route("/workouts", methods=["POST"])
def create_workout():
    try:
        data = workout_schema.load(request.json)

        workout = Workout(**data)

        db.session.add(workout)
        db.session.commit()

        return workout_schema.dump(workout), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 400


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return {"error": "Workout not found"}, 404

    db.session.delete(workout)
    db.session.commit()

    return {}, 204


# -------------------------
# EXERCISE ROUTES
# -------------------------

@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    return exercises_schema.dump(exercises), 200


@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    return exercise_detail_schema.dump(exercise), 200


@app.route("/exercises", methods=["POST"])
def create_exercise():
    try:
        data = exercise_schema.load(request.json)

        exercise = Exercise(**data)

        db.session.add(exercise)
        db.session.commit()

        return exercise_schema.dump(exercise), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 400


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    db.session.delete(exercise)
    db.session.commit()

    return {}, 204


# -------------------------
# WORKOUT EXERCISE ROUTE
# -------------------------

@app.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"]
)
def add_exercise_to_workout(workout_id, exercise_id):

    workout = db.session.get(Workout, workout_id)
    exercise = db.session.get(Exercise, exercise_id)

    if not workout:
        return {"error": "Workout not found"}, 404

    if not exercise:
        return {"error": "Exercise not found"}, 404

    try:
        data = request.json or {}

        data["workout_id"] = workout_id
        data["exercise_id"] = exercise_id

        validated_data = workout_exercise_schema.load(data)

        workout_exercise = WorkoutExercise(**validated_data)

        db.session.add(workout_exercise)
        db.session.commit()

        return workout_exercise_schema.dump(workout_exercise), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 400


if __name__ == "__main__":
    app.run(port=5555, debug=True)
