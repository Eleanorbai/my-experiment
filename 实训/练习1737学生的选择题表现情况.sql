SELECT
	exercise_answers.user_id,
	exercise_answers.exercise_question_id,
	exercise_choices.choice_text,
	exercise_choices.choice_position,
	exercise_answers.created_at
FROM
	exercise_answers,
	exercise_choices
WHERE
	exercise_answers.exercise_choice_id = exercise_choices.id and
	exercise_answers.exercise_question_id = exercise_choices.exercise_question_id AND
	exercise_answers.exercise_question_id = 1737