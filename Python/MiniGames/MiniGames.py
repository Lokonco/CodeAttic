#--------IMPORTS--------#
from time import sleep
from random import randint, random
#-----------------------#

#----- Function for Main Menu; returns player_choice -----#
def MenuScreen():
    player_choice = 0

    while player_choice < 1 or player_choice > 3:
        try:
            print("1) See Rules\n2) Play Game\n3) Return to Main Menu")
            player_choice = int(input("Enter your choice: "))
            if player_choice < 1 or player_choice > 3: #If statement to make sure user input is valid 1-3
                print("Invalid Input! PLease enter either 1, 2, or 3")
        # Catch error if user inputs non integer
        except ValueError:
            print("\nInvalid Input! Must be a Integer between 1 and 3\n")

    return player_choice
#---------------------------------------------#

#------------ DICE GAME --------------#
# This is all the logic for the dice game created
#------ Dice Functions ------#
def sideOne():
    print(" ___________")
    print("|           |")
    print("|    ---    |")
    print("|   |   |   |")
    print("|    ---    |")
    print("|___________|")
def sideTwo():
    print(" ___________")
    print("|       _   |")
    print("|      |_|  |")
    print("|   _       |")
    print("|  |_|      |")
    print("|___________|")
def sideThree():
    print(" ___________")
    print("|        _  |")
    print("|     _ |_| |")
    print("|  _ |_|    |")
    print("| |_|       |")
    print("|___________|")
def sideFour():
    print(" ___________")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|___________|")
def sideFive():
    print(" ___________")
    print("|  _     _  |")
    print("| |_| _ |_| |")
    print("|  _ |_| _  |")
    print("| |_|   |_| |")
    print("|___________|")
def sideSix():
    print(" ___________")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|___________|")
#--------------------------#

#------- Function for displaying dice -------#
def diceDisplay():
    diceNum = 0
    diceNum = randint(1, 6) #Generate random number 1-6

    #-----Display Dice-----#
    if diceNum == 1:
        sideOne()
    elif diceNum == 2:
        sideTwo()
    elif diceNum == 3:
        sideThree()
    elif diceNum == 4:
        sideFour()
    elif diceNum == 5:
        sideFive()
    elif diceNum == 6:
        sideSix()
    #--------------------#
    return diceNum
#-------------------------------------------#

#----- Function for Dice Game -----#
def GuessTheRoll():
    rounds = 5 # Const for amount of game rounds
    menu_selection = diceSum = playerGuess = diceOne = diceTwo = score = compScore = 0

    #-----TitleScreen-----#
    print("\nHello Welcome to my Dice Game\n")
    sleep(1)
    print("Guess\n")
    sleep(1)
    print("The\n")
    sleep(1)
    print("Sum\n")
    sleep(1)
    #-------------------#

    #-------Display Menu---------#
    while menu_selection != 3:
        menu_selection = MenuScreen()

        if menu_selection == 1: #Rules
            print(f"\n{'*' * 40}")
            print("\nThe player tries to guess what the sim of the 2 dice thrown will be")
            print("If the player guess right they earn a point. if not the computer gets a point")
            print("Highest score after 5 rounds wins\n")
            print(f"\n{'*' * 40}")

        elif menu_selection == 2: #Play Game
            score = compScore = 0
            for x in range(rounds):
                playerGuess = 0 #Reset player guess to seed loop

                #------Display Round #-----#
                print(f"\n{'*'*40}")
                print(f"Round {x+1}".center(40)+"\n")
                print(f"\n{'*' * 40}")

                #----- Prompt User for input -----#
                while playerGuess < 2 or playerGuess > 12:
                    try:
                        playerGuess = int(input("\nPlease guess a sum of the 2 dice (2-12): "))
                        if playerGuess < 2 or playerGuess > 12:
                            print("\nInvalid Input! PLease enter a guess between 2 and 12")
                    except ValueError:
                        print("\nMust be a Integer Value\n")

                #----- Roll Dice -----#
                sleep(1)
                print("\nHere comes the first roll...")
                sleep(.5)
                diceOne = diceDisplay()
                print("\nHere comes the second roll...")
                sleep(.5)
                diceTwo = diceDisplay()
                #---------------------#

                #-----Sum Rolls & Give Points -----#
                diceSum = diceOne + diceTwo #Var for dice total
                print(f"\nThe roll total is:  {diceSum}")

                # If user input is correct give point; Else give computer point
                if playerGuess == diceSum:
                    print(f"\nYour guess was {playerGuess} - You were Correct!!")
                    score += 1
                else:
                    print(f"\nYour guess was {playerGuess} - You were Incorrect :(")
                    compScore += 1

                # Print Points
                print(f"\nCurrent score: Player: {score}\nComputer: {compScore}\n")
            #------------------------#

            #---Game over logic---#
            if score > compScore:
                print(f"All rounds are finished. The winner is Player!")
            else:
                print(f"\nThe winner is Computer!")
        #print(f"All rounds are finished. The winner is {'Player' if score > compScore else 'Computer'}!") #Game over logic using ternary operator
            #---------------------------#

    else:# User inputs 3; Exit back to main menu
        print("\nThanks for playing the Guess The Sum Game!\n")
#--------------------------------------------------------------#


#----------------- High Card Wins Game --------------------------#
# This is all the logic for the Card game
def HighCardWins(name):
    #----------Create Cards-------#
    cardRanks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] # We define the ranks of cards in a list
    suit = "♣" # Define the suit
    # Here we make a template for what our card will look like / Same style as cards from cafe
    card_template = """*- - -*
| {suit}   |
| {rank:^3} |
|   {suit} |
*- - -*"""
    # Here we create the cards using format and a for in loop and store in cardList[]
    cardList = [card_template.format(suit=suit, rank=rank) for rank in cardRanks]
    #-----------------------------#

    #Variables
    winner = ""
    playerCard = menuSelection = compCard = playerScore = compScore = turn = 0

    #-----Title Screen-----#
    print("\nWelcome to the High Cards\n")
    print("High\n")
    sleep(1)
    print("Card\n")
    sleep(1)
    print("Wins")
    sleep(1)
    #----------------------#

    #-----Display Menu-----#
    while menuSelection != 3:
        playerScore = compScore = turn = 0
        menuSelection = MenuScreen()
        if menuSelection == 1: # Player selected rules
            print(f"\n{'*' * 40}")
            print("\nThe player draws a card.\nThen the computer draws a card.\nThen the highest card is the winner")
            print(f"\n{'*' * 40}")

        elif menuSelection == 2: # Player selected to play game
            while playerScore != 5 and compScore != 5: # Loop until someone gets 5 points
                #Display current round & Introduce player using parameter
                turn += 1
                print(f"Round {turn}".center(40, '♣'))
                input(f"Are you ready to play {name}?, Press Enter to Continue...")
                sleep(.5)

                # Generate rand card for player and computer
                playerCard = randint(0, 12)
                compCard = randint(0, 12)

                #-----Display Cards-----#
                print("Player card:")
                print(cardList[playerCard])
                sleep(.5)
                print("\nIt is now the computers turn...\n")
                sleep(.5)
                print("Computer card:")
                print(cardList[compCard])
                sleep(.5)
                #-----------------------#

                #-----Point System-----#
                if playerCard < compCard: # less than is used since lower index = higher card
                    playerScore += 1
                    print(f"\nThe winner of round {turn} is {name}")
                elif compCard < playerCard:
                    compScore += 1
                    print(f"\nThe winner of round {turn} is the Computer")
                else:
                    print(f"\nRound {turn} is a TIE!")
                #----------------------#

                print(f"Running score after round {turn}:\n{name:<12} {playerScore}\nComputer score: {compScore}")
                sleep(.5)

                #-----Display Winner-----#
                if playerScore == 5:
                    print(f"Game Over!\nThe winner is {name} :)\n")
                elif compScore == 5:
                    print(f"Game Over!\nThe winner is the Computer :(\n")
                #------------------------#

        else: # Player exited back to menu
            print("Thanks for playing")
#-------------------------------------------------------------#


#--------------------Trivia Game--------------------#
def TriviaGame(name):
    category = questionAns = ""
    menuSelection = score = 0

    #---------- Catogrozied lists with questions ----------#
    pythonQuestions = [
        ["What keyword is used to define a function in Python?", ["def", "function", "define", "func"], "A"],
        ["What does the len() function return?", ["The last element", "The length of an object", "The first element", "The type of object"], "B"],
        ["How do you get user input in Python?", ["getLine()", "input()", "read()", "cin"], "B"],
        ["Which data type is immutable in Python?", ["list", "dictionary", "set", "tuple"], "D"],
        ["What does 'elif' stand for in Python?", ["else if", "end if", "equal if", "execute if"], "A"]
        ]
    popCultureQuestions = [
        ["What streaming service produced 'Stranger Things'?", ["Hulu", "Amazon Prime", "Netflix", "Disney+"], "C"],
        ["Which artist has won the most Grammy Awards?", ["Beyoncé", "Taylor Swift", "Adele", "Michael Jackson"], "A"],
        ["Which rapper is known as 'Yeezy'?", ["Drake", "Kanye West", "Travis Scott", "Kid Cudi"], "B"],
        ["Which group released the album 'Straight Outta Compton'?", ["Public Enemy", "N.W.A", "Wu-Tang Clan", "Run-DMC"], "B"],
        ["Which rapper is known for the album 'The Chronic'?", ["Snoop Dogg", "Dr. Dre", "Ice Cube", "Eazy-E"], "B"]
        ]
    logicQuestions = [
        ["Complete: 1, 4, 9, 16, ?", ["20", "25", "24", "21"], "B"],
        ["If A = 1, B = 2, C = 3, what does CAB equal?", ["6", "321", "123", "312"], "B"],
        ["What comes next in the sequence: 2, 6, 12, 20, 30, ?", ["40", "42", "38", "44"], "B"],
        ["Tom is taller than Sam. Sam is taller than Joe. Who is shortest?", ["Tom", "Sam", "Joe", "Can't tell"], "C"],
        ["What's missing: Red, Blue, Green, ?", ["Yellow", "Orange", "Purple", "Black"], "A"]
        ]
    #------------------------------------------------#

    # Display Title
    print("" + "*" * 30)
    print("Welcome to trivia!")

    #Display Menu
    while menuSelection != 3:
        score = 0
        category = ""
        menuSelection = MenuScreen()

        if menuSelection == 1: # Rules
            print(f"\n{'?'*40}")
            print("\nRules: Answer question correct gain 10 points else lose 5 points\n")
            print(f"\n{'?' * 40}")
        elif menuSelection == 2: # Play Game
            while category != "A" and category != "B" and category != "C":
                category = input("\nChoose a category:\nA)Python\nB)Pop-Culture\nC)Logic\nSelection: ").strip().upper()

                #-----Logic for choosing category-----#
                if category == "A":
                    questionList = pythonQuestions
                elif category == "B":
                    questionList = popCultureQuestions
                elif category == "C":
                    questionList = logicQuestions
                else:
                    print("Invalid category, Please choose A-C")
                    continue
                #-------------------------------------#

                #-----Show questions and ans-----#
                for question in questionList:
                    questionAns = ""
                    while questionAns not in ["A", "B", "C","D"]: #Ask player for answer and validate
                        print(f"\n{question[0]}\nA){question[1][0]}\nB){question[1][1]}\nC){question[1][2]}\nD){question[1][3]}")
                        questionAns = input("Please select your answer: ").strip().upper()

                        #----------Validate----------#
                        if questionAns not in ["A", "B", "C","D"]: #Invalid input
                            print(f"\nPlease read {name}...Must choose A,B,C or D!\n")
                        elif questionAns == question[2]: # Player is correct
                            sleep(.5)
                            print("That answer is...")
                            print("Correct!\n")
                            score += 10
                        else: # Player is incorrect
                            sleep(.5)
                            print("That answer is...")
                            print("Incorrect!\n")
                            score -= 5
                        #---------------------------#

                        # Show running score
                        print(f"The current score is {score}/50\n")

                #-----Show Final Score-----#
                if score > 30:
                    print(f"\nGreat Job {name}! - Final Score: {score}/50\n")
                    print("" + "*" * 30)
                elif score > 10:
                    print(f"\nFair Try {name}! - Final Score: {score}/50\n")
                    print("" + "*" * 30)
                else:
                    print(f"Welp, {name}- Final Score: {score}/50\n")
                    print("" + "*" * 30)
                #---------------------------#

        else: # Exit
            print("Thanks for playing!\n")
#---------------------------------------------------#


#--------------------Math Game--------------------#
def MathGame(name):
    questionAns = ""
    menuSelection = score = 0

    #----------List with math questions----------#
    # Group questions by difficulty and store in sublist like we did with trivia
    # Each List contains 10 questions
    easyQuestions = [
        ["What is 5 + 3?", ["6", "7", "8", "9"], "C"],
        ["What is 10 × 2?", ["15", "20", "25", "30"], "B"],
        ["What is 45 ÷ 9?", ["4", "5", "6", "7"], "B"],
        ["What is half of 50?", ["20", "25", "30", "15"], "B"],
        ["What is the value of 10²?", ["100", "20", "200", "10"], "A"],
        ["What is 7 × 8?", ["54", "56", "58", "60"], "B"],
        ["What is 90 − 45?", ["40", "42", "45", "50"], "C"],
        ["What is 100 ÷ 10?", ["5", "10", "15", "20"], "B"],
        ["What is the smallest prime number?", ["0", "1", "2", "3"], "C"],
        ["What is 11 + 14?", ["24", "25", "26", "27"], "B"]]
    mediumQuestions = [
        ["What is 10³?", ["100", "1000", "10,000", "1,000,000"], "B"],
        ["What is 5² + 4²?", ["30", "41", "45", "50"], "B"],
        ["If x = 7, what is 3x + 5?", ["21", "24", "26", "29"], "D"],
        ["What is (6² ÷ 3) + 4?", ["14", "16", "18", "20"], "B"],
        ["What is 100 ÷ (5 × 4)?", ["4", "5", "10", "20"], "A"],
        ["What is ¾ of 100?", ["25", "50", "75", "80"], "C"],
        ["What is (15 × 2) + 10?", ["30", "35", "40", "45"], "C"],
        ["What is the cube root of 27?", ["2", "3", "4", "5"], "B"],
        ["What is 20% of 450?", ["80", "85", "90", "100"], "C"],
        ["What is (18 ÷ 3) × 4?", ["20", "22", "24", "26"], "C"]]
    hardQuestions = [
        ["Solve: (5 × 6) − (8 ÷ 2)", ["26", "27", "28", "29"], "C"],
        ["If a car travels 60 km in 1.5 hours, what is its speed?", ["30 km/h", "40 km/h", "50 km/h", "60 km/h"], "C"],
        ["What comes next in the sequence: 2, 6, 12, 20, 30, ?", ["40", "42", "38", "44"], "B"],
        ["What is the next prime number after 29?", ["30", "31", "33", "37"], "B"],
        ["What is the sum of angles in a triangle?", ["90°", "120°", "180°", "360°"], "C"],
        ["What comes next: 2, 4, 8, 16, ?", ["20", "24", "32", "64"], "C"],
        ["What is the value of √81 + √16?", ["15", "17", "18", "19"], "B"],
        ["Which is larger: 3³ or 4²?", ["3³", "4²", "They are equal", "Cannot compare"], "A"],
        ["What is 2⁵?", ["32", "64", "16", "25"], "A"],
        ["What is the value of π (Pi) to 2 decimal places?", ["3.12", "3.14", "3.15", "3.13"], "B"]]
    #-------------------------------------------#

    # Display Title
    print("" + "*" * 30)
    print("Welcome to Math Trivia")

    # Display Menu
    while menuSelection != 3:
        score = totalQuestions =  0
        category = ""
        menuSelection = MenuScreen()

        #----- Logic for menu selection ------#
        if menuSelection == 1:  # Rules
            print(f"\n{'?' * 40}")
            print("Rules: Answer question correct gain points Easy - 5, Medium - 10, Hard - 15")
            print("If you answer incorrectly, You will lose points depending on difficulty")
            print("Easy -2, Medium -5, Hard -7")
            print("Answer 10 questions or get to 50 points and you WIN!")
            print(f"\n{'?' * 40}")

        #-------------PLAY GAME LOGIC------------#
        elif menuSelection == 2:
            while score < 50 and totalQuestions < 10:
                category = "" #Reset diff so player can choose either easy,med,hard
                while category not in ["A","B","C"]:
                    category = input("What category do you want to choose?\nA) Easy\nB) Medium\nC) Hard\n").strip().upper()

                    # Validate Input
                    if category not in ["A","B","C"]:
                        print("Invalid category, please choose either A, B, or C")

                #Get question and remove question
                if category == "A":
                    questionIndex = randint(0,len(easyQuestions)-1)
                    question = easyQuestions.pop(questionIndex)
                elif category == "B":
                    questionIndex = randint(0, len(mediumQuestions) - 1)
                    question = mediumQuestions.pop(questionIndex)
                elif category == "C":
                    questionIndex = randint(0, len(hardQuestions) - 1)
                    question = hardQuestions.pop(questionIndex)

                questionAns = ""
                while questionAns not in ["A", "B", "C", "D"]:
                    print(f"\n{question[0]}\nA){question[1][0]}\nB){question[1][1]}\nC){question[1][2]}\nD){question[1][3]}")
                    questionAns = input("\nWhat is your answer? ").strip().upper()

                    # Validate response
                    if questionAns not in ["A", "B", "C", "D"]:
                        print("Invalid answer, please choose either A, B, or C")

                    elif questionAns == question[2]:
                        sleep(.5)
                        print("That answer is Correct.")
                        if category == "A": #If diff is easy give 5 points
                            score += 5
                        elif category == "B":  #If diff medium is  give 10 points
                            score += 10
                        elif category == "C":  #If diff is hard give 15 points
                            score += 15
                    else:
                        print("That answer is Incorrect.")
                        if category == "A":  # Easy -2
                            score -= 2
                        elif category == "B":  # Medium -5
                            score -= 5
                        elif category == "C":  # Hard -7
                            score -= 7
                totalQuestions += 1
                print(f"The current score is {score}")

            #Game over
            print(f"\n{'?' * 30}")
            if score >= 50:
                print("Congratulations! You won!")
            else:
                print(f"\nGame Over! Not 50 points but your Final Score was: {score}\n")

        #Player quits game
        else:
            print("Thanks for playing!\n")
        #------------------------------------#
#-------------------------------------------------#


#-------- Main Function ---------#
def main():
    name = menuChoice = ""
    print("WELCOME TO MY MINI-GAME ARCADE!!!") #Title screen

    #Ask user for name & prompt to choose a game
    name = input("Enter your name: ")
    print(f"Hello {name}, are you ready to play?")
    sleep(.5)
    print("Choose a game to play from the menu below")

    while menuChoice != 5:
        print("" + "*" * 30)
        print("\t-----Mini Games-----")
        print("\t1) Guess The Roll\n\t2) High Card Wins\n\t3) Trivia Game\n\t4) Math Game\n\t5) Exit")
        print("" + "*" * 30)
        menuChoice = input("\nEnter your choice: ")

        #-----Logic for choosing option-----#
        if menuChoice == "1":
            print("Good choice... Let's play!\n")
            sleep(.5)
            GuessTheRoll()
        elif menuChoice == "2":
            print("Good choice... Let's play!\n")
            sleep(.5)
            HighCardWins(name)
        elif menuChoice == "3":
            print("Good choice... Let's play!\n")
            sleep(.5)
            TriviaGame(name)
        elif menuChoice == "4":
            print("Good choice... Let's play!\n")
            sleep(.5)
            MathGame(name)
        elif menuChoice == "5":
            print(f"Thanks for playing {name}... Goodbye!")
        else:
            print("Please select a valid option (1-5)")
        #-----------------------------------#
#-----------------------------#
main()
