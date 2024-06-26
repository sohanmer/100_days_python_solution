class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        self.check_score(current_question, user_input)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_score(self, question, user_input):
        if question.answer.lower() == user_input.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
