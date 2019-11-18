# from questions import MultipleChoiceQuestions, NumericalAnswerQuestions, BooleanQuestions

transformers = 'Transformers Quiz'
capitals = 'Capitals Quiz'
trump_quotes = 'Trump Quotes Quiz'
letters = ["a", "b", "c", "d", "e"]



def get_quiz_choice():
    while True:
        try:
            quiz_number = int(raw_input(
                'Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(transformers_questions, capitals_questions, trump_quotes_questions)))
        except ValueError:
            print ("Not a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print ("Invalid value, please try again\n")
            else:
                return quiz_number


def ask_multiple_choice():
    
    
    letters = ["a", "b", "c", "d", "e"]
    guess = input
    if guess not in letters:
        print (f"Not a valid entry. Please try again. ")
    
def ask_numeric_response():
    guess = input
    answer = (quiz.question.answer)
    if guess == answer:
        print (f"Correct")
    else:
        print (f"Incorrect")
    
    
def ask_boolean():
    guess = input
    answer = (quiz.question.answer)
    if guess == answer:
        print (f"Correct")
    else:
        print (f"Incorrect")
    

quizzes = [transformers, capitals, trump_quotes]

def transformers_quiz():
        print ("Welcome to the Transformers: The Movie Fan Quiz. How much do you really know about the cult classic cartoon?\n")

def trans_q_1():
        response = input("Question 1\n Transformers: The Movie came out in which year?\n a: 1984\n b: 1985\n c: 1986\n d: 1987\n e: 2007\n Enter a letter a-e\n")
        
        if response == "C":
            print("That's right!")
            return 1
        else: 
            print("Sorry, the correct answer is C) 1977")
            return 0
        
        # (1986)
        
#         print("Question 2\n Orson Welles' last ever performance in a movie came as he voiced the character of:\n" )

#         trans_q_2_dict = {
#         a: "Optimus Prime",
#         b: "Megatron",
#         c: "Galvatron",
#         d: "Unicron",
#         e: "Ultra Magnus"
#         }

#         # (Unicron)

#         print("Question 3\n Wreck-Gar was played my which former member of Monty Python?\n" )

#         trans_q_3_dict = {
#         a: "John Cleese",
#         b: "Terry Jones",
#         c: "Michael Palin",
#         d: "Eric Idle",
#         e: "Terry Gilliam"
#         }
        

#         # (Eric Idle)

#         print("Question 4\n Which Autobot convinces the Sharkticons to turn on their masters?\n")

#         trans_q_4_dict = {
#         a: "Hot Rod",
#         b: "Kup",
#         c: "Grimlock",
#         d: "Slagg",
#         e: "Blurr"
#         }
        
#         # (Grimlock)
        
        

#         print("Question 5\n How many Decepticons does Optimus Prime take out when he returns to Earth and halts the seige of Autobot City, before facing Megatron?\n")


#         # (8)

#         print("Question 6\n Stan Bush had how many hit songs on the soundtrack to the movie?\n")

#         # (2)

#         print("Question 7\n '_____________ shall stand _____________ shall fall.'\n Complete the catchphrase with the appropriate number.\n")


#         # (1)

#         print("Question 8\n Which Decepticon sought to crown himself leader after the apparent demise of Megatron?\n")

#         trans_q_8_dict = {
#         a: "Starscream",
#         b: "Soundwave",
#         c: "Shockwave",
#         d: "Devastator",
#         e: "Cyclonus"
#         }
        

#         # (Starscream)

#         print("Question 9\n The Autobot symbol of leadership had the same name as a hit movie series 'The Matrix' decades later. True or False?\n")


#         # (True)

#         print("Question 10\n The home planet of the Transformers is called Robotron. True or False?\n")

#         # (False)


#     # checks if user input is in correct format
#     # guess = input("Guess ONE letter, a-e: ")
#     # if len(guess) > 1: # checks if guess is more than one character
#     #         print (f"Not a valid entry. Please try again. ")
#     #     if not guess.isalpha(): #checks if guess is an alphabetic letter
#     #         print (f"Not a valid entry. Please try again. ")
#     #     #TODO: Check if the guessed letter is in the secret_word or not and give the player feedback
            
#         # if guess == answer
#         #     score += 1
            
#         # elif not guess.isalpha() or len(guess) > 1: #checks whether guess is not alphabetic, is longer than one character
#         #     score = score #update score variable 
        



# def capitals_quiz():
#         print ("Welcome to the Capital Cities of the World Quiz. Test your knowledge of historical and current capital cities.\n")
        
#         print("Question 1\n The former capital of the Ottoman Empire was named after which Roman Emperor?\n")

#         caps_q_1_dict = {
#         a: "Augustus",
#         b: "Ankaraticus",
#         c: "Constantine",
#         d: "Hadrian",
#         e: "Istanbullion"
#         }

#         # (Constantine)

#         print("Question 2\n Tripoli is the capital of Algeria. True or False?\n")

#         # (False)

#         print("Question 3\n The capital of Scotland is Edinburgh. True or False?\n")

#         # (True)

#         print("Question 4\n Name the first capital of Japan:\n")

#         caps_q_4_dict = {
#         a: "Tokyo",
#         b: "Edo",
#         c: "Nara",
#         d: "Kyoto",
#         e: "Nagaoka"
#         }
#         # (Nara)

#         print("Question 5\n What year did Bonn become the capital of the Federal German Republic?\n")

#         number

#         # (1949)

#         print("Question 6\n In what year did Brazil move its capital from Rio de Janiero to Brasilia?\n")

#         number

#         # (1960)

#         print("Question 7\n In which year did Peking officially start to change the foreign pronunciation of its name back to Beijing?\n")

#         number

#         # (1949)

#         print("Question 8\n Beijing is the world's most populated capital city, but which city comes in at number 2?\n")

#         caps_q_8_dict = {
#         a: "New Delhi",
#         b: "Tokyo",
#         c: "Manila",
#         d: "Moscow",
#         e: "Cairo"
#         }
        
#         # (New Delhi)

#         print("Question 9\n Ngerulmud, the capital city of the Pacific island nation of Palau, is the world's least populated national capital. What is its population range?\n")

#         caps_q_9_dict = {
#         a: "0-199",
#         b: "200-399",
#         c: "400-599",
#         d: "600-799",
#         e: "800-1000"
#         }
        

#         # (b)

#         print("Question 10\n Hungary's capital city Budapest used to be two cities. True or False?\n")

#         # (True)




# def trump_quotes_quiz():
#             print ("Welcome to the Trump Quotes Quiz. Answer questions about (alleged) lies by the former 'Apprentice' reality TV star.")

# print("Question 1\n 'The reason Russia was in Afghanistan was because {} were going into Russia:'\n")

#     trump_q_1_dict = {
#         a: "terrorists",
#         b: "immigrants",
#         c: "nuclear weapons",
#         d: "drug dealers",
#         e: "feminists"
#         }

#         # (a)

#         print("Question 2\n 'In the ‘old days’ if you were president and you had a good {}, you were basically immune from criticism.'\n")

#         trump_q_2_dict = {
#         a: "credit report",
#         b: "suit",
#         c: "dog",
#         d: "tv rating",
#         e: "economy"
#         }
        

#         # (e)


#         print("Question 3\n 'The noise (from windmills) causes cancer.' True or False?\n")

#         # (False)

#         print("Question 4\n 'In California, 'they're rioting now' over sanctuary cities.' True or False?\n")

#         # (False)

#         print("Question 5\n 'I think the only difference between me and the other candidates is that I'm more {} and my women are more beautiful.'\n")

#         trump_q_5_dict = {
#         a: "intelligent",
#         b: "good-looking",
#         c: "stable",
#         d: "rich",
#         e: "honest"
#         }


#         # (honest)

#         print("Question 6\n 'Heidi Klum. Sadly, she's no longer a {}.'\n")

#         number input

#         # (10)

#         print("Question 7\n 'When Hillary Clinton 'ran the State Department, ${} billion was missing. How do you miss ${} billion? You ran the State Department, ${} billion was either stolen — they don't know.''\n")

#         number input

#         # (6)

#         print("Question 8\n 'Our African-American communities are absolutely in the worst shape they've ever been in before: Ever. Ever. Ever.' True or False?\n")

#         # (False)

#         print("Question 9\n 'Out of 67 counties (in Florida), I won {}, which is unprecedented: It's never happened before.'\n")

#         number input

#         # (66)

#         print("Question 10\n 'The unemployment rate may be as high as '42 percent.'' True or False?\n")

#         # (False)



def run_quiz():
    total_score = 0

    response = input('Do you want to take a quiz on [1] Transformers: The Movie, or [2] capital cities or [3] Trump quotes?\n Type transformers, cities or Trump.\n')
    if input == 'transformers':
        transformers_quiz()
    elif input == 'cities':
        capitals_quiz()
    elif input == 'trump':
        trump_quotes_quiz()
    return
        # print ("Would you like to play again? If so, enter 'yes'.")
        # while input() == "yes": run_quiz()
    

run_quiz()