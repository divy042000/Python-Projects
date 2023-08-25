import random
word_list = ["APPLE","ORANGE","CHERRY","WATER","CARBON"]
def  get_word():
     word=random.choice(word_list)
     return word.upper()
def play(word):
    word_completed="_"*len(word)
    yourguess=False
    guessedletters=[]
    guessedwords=[]
    tries=6
    print("Lets Play Hangman !")
    print()
def display_hangman(tries):
    stages=[""""
            --------
            |       |
            |       O
            |     \\\|/
            |       | 
            -      / \\
            """,
            """
            --------
            |       |
            |       O
            |     \\\|/
            |       | 
            -      / 
            """,
                """
            --------
            |       |
            |       O
            |     \\\|/
            |       | 
            -      
            """,
               """
            --------
            |       |
            |       O
            |     \\\|
            |       | 
            -      
            ""","""
            --------
            |       |
            |       O
            |       |
            |       | 
            -       
            """,
            """
            --------
            |       |
            |       O
            |       
            |       
            -   
            """,
            """
            --------
            |       |
            |           
            |     
            |        
            -      
            """,
        ]
    return stages[tries]
   