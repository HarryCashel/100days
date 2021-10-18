import html

class QuizBrain:
    """Models the quiz and logic"""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.high_score = 0
        self.current_question = None

    def next_question(self):
        """Moves the quiz to the next question"""
        self.current_question = self.question_list[self.question_number]
        question_text = html.unescape(self.current_question)
        self.question_number += 1

    def check_answer(self):
        """Checks user guess against question answer"""
        pass

    def have_questions(self):
        return self.question_number < len(self.question_list)