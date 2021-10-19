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
        if self.have_questions():
            self.current_question = self.question_list[self.question_number]
            question_text = html.unescape(self.current_question.question)
            self.question_number += 1
            return f"Q.{self.question_number}:{question_text}"
        else:
            pass

    def check_answer(self, user_answer):
        """Checks user guess against question answer"""
        if user_answer == self.current_question.answer:
            self.score += 1
            print("correct")
            return True
        else:
            print("wrong")
            return False

    def have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False
