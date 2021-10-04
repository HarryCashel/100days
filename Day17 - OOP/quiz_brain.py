# ask question
# check if correct
# end of quiz?

from clear_screen import screen_clear as clear
import time


class QuizBrain:
    """Models the Quiz"""
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Moves the quiz to the next question"""
        current_question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number + 1}. {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        """Checks user input against question answer"""

        if user_answer.lower() in correct_answer.lower().strip():
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer was {correct_answer}.")
        print(f"Current score: {self.score}")
        time.sleep(1)
        clear()

