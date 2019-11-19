questions = ["Welcome to the Transformers: The Movie Quiz!\n 1. Transformers: The Movie came out in which year?\n Enter a letter between a-e, or type out the answer.",
            "\n2. Orson Welles' last ever performance in a movie came as he voiced the character of:\n Enter a letter between a-e, or type out the answer.",
            "\n3. Wreck-Gar was played my which former member of Monty Python?\n Enter a letter between a-e, or type out the answer.",
            "\n4. Which Autobot convinces the Sharkticons to turn on their masters?\n Enter a letter between a-e, or type out the answer.",
            "\n5. How many Decepticons does Optimus Prime take out when he returns to Earth and halts the seige of Autobot City (before facing Megatron)?\n Enter and integer.",
            "\n6. Stan Bush had how many hit songs on the soundtrack to the movie?\n Enter and integer.",
            "\n7. '_____________ shall stand, _____________ shall fall.'\n Complete the catchphrase with the appropriate number.",
            "\n8. Which Decepticon sought to crown himself leader after the apparent demise of Megatron?\n Enter a letter between a-e, or type out the answer.",
            "\n9. The Autobot symbol of leadership had the same name as a hit movie series 'The Matrix', over a decade later. True or False?\n Enter 1 for True, or 0 for False.",
            "\n10. The home planet of the Transformers is called Robotron. True or False?\n Enter 1 for True, or 0 for False."
]
    


answer_choices = [" a: 1984\n b: 1985\n c: 1986\n d: 1987\n e: 2007\n Your Answer:",
                "a: Optimus Prime\n b: Megatron\n d: Unicron\n e: Ultra Magnus\n Your Answer:",
                "a: John Cleese\n b: Terry Jones\n d: Michael Palin\n e: Eric Idle\n Terry Gilliam\n Your Answer:",
                "a: Hot Rod\n b: Kup\n d: Grimlock\n e: Slagg\n Blurr\n Your Answer:",
                "Enter an integer\n Your Answer:",
                "Enter an integer\n Your Answer:",
                "Enter an integer\n Your Answer:",
                " a: Starscream\n b: Soundwave\n c: Shockwave\n d: Devastator\n e: Cyclonus\n Your Answer:",
                "Enter 1 for True, 0 for false\n Your Answer:",
                "Enter 1 for True, 0 for false\n Your Answer:"
]

correct_answers = [{"c", "1986"},
                    {"d", "Unicron"},
                    {"d", "Eric Idle"},
                    {"c", "Grimlock"},
                    {"8"},
                    {"2"},
                    {"1", "One"},
                    {"a", "Starscream"},
                    {"1", "true"},
                    {"0", "false"}
]

answers = ["It was released in 1986",
            "Unicron",
            "Eric Idle",
            "Grimlock",
            "8",
            "2",
            "One shall stand, one shall fall.",
            "Starscream",
            "The answer is True",
            "The answer is False"
]

def run_quiz():
    total_score = 0
    for question, choices, correct_answer, answer in zip (questions, answer_choices, correct_answers, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_answer:
            print("Correct")
            total_score+=1
        else:
            print("Incorrect", answer)
    print("\n     Correctly answered", total_score, "out of 10.")
    
    
    
run_quiz()
