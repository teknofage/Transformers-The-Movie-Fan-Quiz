# Question:
# Question: Gideon's mom's name is Judith, true or false?


def question_one():
    """Asks a true or false question"""
    
    response = int(input("Gideon's mom's name is Judith. true or false? Enter a 0 for false and a 1 for true. \n"))
    correct_answer = 1
    
    if response == correct_answer:
        print("You got it!")
        total_score += 1
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        return 0
    
    # code to run the quiz
    total_score = 0
    result = question_one()
    total_score += result
    print(total_score)
    
    question_one()