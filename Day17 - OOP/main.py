from data import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(i['question'], i['correct_answer']) for i in data]

quiz = QuizBrain(question_bank)

while quiz.question_number < 12:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your score was {quiz.score}/12")
