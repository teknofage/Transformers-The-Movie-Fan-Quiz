# Classes of Questions
import random

class MultipleChoiceQuestions:
    def __init__(self, question, answer, options=[strings]):
        self.question = questions
        self.answer = answer
        self.wrong = options
        
    def verify(self, user_input):
        return user_input == self.answer
    def display(self):
        random_index = random.randint(0,4)
        options = self.wrong
        options.insert(random_index, self.answer)
        letters = ["a", "b", "c", "d", "e"]
        op_dict = dict(zip(letters, options))
        for letter, option in op_dict.itmes():
            print(f"{letter}. - {option}")
        user_input = input("Enter a letter: a, b, c, d, e")
        answer = op_dict[user_input]
        self.verify(answer)


class NumericalAnswerQuestions



class BooleanQuestions