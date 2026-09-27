from marshmallow import Schema, fields, validate


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )

    sets = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=50)
    )

    equipment_needed = fields.Bool(required=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    notes = fields.Str(allow_none=True)


class WorkoutDetailSchema(WorkoutSchema):
    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        dump_only=True
    )

    exercises = fields.Nested(
        ExerciseSchema,
        many=True,
        dump_only=True
    )


class ExerciseDetailSchema(ExerciseSchema):
    workouts = fields.Nested(
        WorkoutSchema,
        many=True,
        dump_only=True
    )
