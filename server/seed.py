from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():
    print("Resetting database...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")

    pushups = Exercise(
        name="Push Ups",
        category="Chest",
        equipment_needed=False
    )

    squats = Exercise(
        name="Squats",
        category="Legs",
        equipment_needed=False
    )

    bench_press = Exercise(
        name="Bench Press",
        category="Chest",
        equipment_needed=True
    )

    db.session.add_all([
        pushups,
        squats,
        bench_press
    ])

    db.session.commit()

    print("Creating workouts...")

    workout1 = Workout(
        date=date(2026, 9, 20),
        duration_minutes=45,
        notes="Upper body workout"
    )

    workout2 = Workout(
        date=date(2026, 9, 21),
        duration_minutes=30,
        notes="Leg day"
    )

    db.session.add_all([
        workout1,
        workout2
    ])

    db.session.commit()

    print("Adding exercises to workouts...")

    workout_exercise1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=pushups.id,
        reps=15,
        sets=3
    )

    workout_exercise2 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=bench_press.id,
        reps=10,
        sets=4
    )

    workout_exercise3 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=squats.id,
        reps=12,
        sets=3
    )

    db.session.add_all([
        workout_exercise1,
        workout_exercise2,
        workout_exercise3
    ])

    db.session.commit()

    print("Seeding complete!")
