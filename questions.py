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
        
        if bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
        else:
            result["Incorrect"] += 1
            return False


class NumericalAnswerQuestions:
    def __init__(self, question, answer):
        self.question = questions
        self.answer = answer
        


    def verify(self, user_input):
        return user_input == self.answer


class BooleanQuestions:
    def __init__(self, question, answer, options=[True or False]):
        self.question = questions
        self.answer = answer
        
    def verify(self, user_input):
        return user_input == self.answer
    
        while True:
                try:
            print "Q: {}".format(question)
            answer = int(raw_input("1 for True\n0 for False\nYour answer: "))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if answer is not 0 and answer is not 1:
                print "Invalid value, please try again\n"
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False
    