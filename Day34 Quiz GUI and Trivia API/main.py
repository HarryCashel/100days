from data import data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(question["question"], question["correct_answer"]) for question in data]

quiz = QuizBrain(question_bank)
# interface = QuizInterface()

if quiz.have_questions():
    pass
print(quiz.next_question())
print(quiz.check_answer("True"))
