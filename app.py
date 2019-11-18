questions = [
    
]
    


answer_choices = [
    
    
]


def run_quiz():
    total_score = 0
    for question, choices, correct_choice, answer in zip (questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()