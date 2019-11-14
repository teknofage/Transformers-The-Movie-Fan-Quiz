

transformers = 'Transformers Quiz'
capitals = 'Capitals Quiz'
trump_quotes = 'Trump Quotes Quiz'
letters = ["a", "b", "c", "d", "e"]

ask_multiple_choice():
    letters = ["a", "b", "c", "d", "e"]
    guess = input
    if guess not in letters:
        print (f"Not a valid entry. Please try again. ")
    
ask_numeric_response():
    guess = input
    answer = (quiz.question.answer)
    if guess == answer:
        print (f"Correct")
    else:
        print (f"Incorrect")
    
    
ask_boolean():
    guess = input
    answer = (quiz.question.answer)
    if guess == answer:
        print (f"Correct")
    else:
        print (f"Incorrect")
    

quizzes = [transformers, capitals, trump_quotes]

def transformers_quiz():
    print ("Welcome to the Transformers: The Movie Fan Quiz. How much do you really know about the cult classic cartoon?")



    # checks if user input is in correct format
    guess = input("Guess ONE letter, a-e: ")
    # if len(guess) > 1: # checks if guess is more than one character
    #         print (f"Not a valid entry. Please try again. ")
    #     if not guess.isalpha(): #checks if guess is an alphabetic letter
    #         print (f"Not a valid entry. Please try again. ")
    #     #TODO: Check if the guessed letter is in the secret_word or not and give the player feedback
            
        if guess == answer
            score += 1
            
        elif not guess.isalpha() or len(guess) > 1: #checks whether guess is not alphabetic, is longer than one character
            score = score #update score variable 
        



def capitals_quiz():
        print ("Welcome to the Capital Cities of the World Quiz. Test your knowledge of historical and current capital cities.")
        
        




def trump_quotes_quiz():
        print ("Welcome to the Trump Quotes Quiz. Choose the missing words from famous (alleged) lies by the former 'Apprentice' reality TV star.")



topic = raw_input('Do you want to take a quiz on Transformers: The Movie, or capital cities or Trump quotes? Type transformers, cities or Trump.')
if topic == 'transformers':
    transformers_quiz()
elif topic == 'cities':
    capitals_quiz()
elif topic == 'trump':
    trump_quotes_quiz()

print ("Would you like to play again? If so, enter 'yes'.")
while input() == "yes": topic()