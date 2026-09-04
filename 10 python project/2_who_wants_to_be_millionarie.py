import random                              # For randomazing questions
from datetime import datetime              # For time
from colorama import Fore, Style, init, Back          # For color
init(autoreset=True)                     # resetting the color

questions = [ ["Which is the biggest planet of our solar system?", "Venus", "Uranus", "Jupiter", "Saturn", 3],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Chennai", "Kolkata", 2],
    ["Who is known as the Father of Computers?", "Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs", 2],
    ["Which language is primarily used for AI and Machine Learning?", "Java", "Python", "C++", "HTML", 2],
    ["How many continents are there on Earth?", "5", "6", "7", "8", 3],
    ["Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["Which keyword is used to define a function in Python?", "func", "define", "def", "function", 3],
    ["What is the chemical symbol of Gold?", "Go", "Au", "Ag", "Gd", 2],
    ["Which country is famous for the Eiffel Tower?", "Italy", "France", "Germany", "Spain", 2],
    ["Who wrote the Indian National Anthem?", "Mahatma Gandhi", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ]

random.shuffle(questions)       # Randomly shuffling questions

prize = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
total_winning = 0 
print("="*40)
print(Fore.CYAN + Style.BRIGHT + "     Who wants to be a millionaire")
print("="*40)
for i, question in enumerate(questions):               # Loop

    print(Fore.WHITE + Style.BRIGHT + Back.BLACK + f"Q {i+1}: {question[0]}")
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    a = int(input("Enter your answer: 1 for a, 2 for b, 3 for c, 4 for d:"))
    
    if question[5] == a:                # If question is right

        total_winning = prize[i]
        print(Fore.GREEN + "Your answer is correct!")
        print(Fore.YELLOW + f"you won: {total_winning}\n")
        if i == len(questions)-1:                   # If all Questions are right
            print('-'*40)
            print(Fore.YELLOW + Style.BRIGHT + f"       Your total winning: {total_winning}")
            with open("your_winnings.txt", "a") as f:              # To print my winnings in txt file
                f.write(f"\n{datetime.now()} ---> ${total_winning}")
            print("="*40)
            print(Fore.BLUE + Style.BRIGHT + "              Game End")
            print("="*40)

    else:          # If wrong option is choosen
        
        print(Fore.RED + f"Wrong answer, the correct answer was: {question[5]}")
        print('-'*40)
        print(Fore.YELLOW + Style.BRIGHT + f"       Your total winning: {total_winning}")
        with open("your_winnings.txt", "a") as f:           # To print my winnings in txt file
            f.write(f"\n{datetime.now()} ---> ${total_winning}")
        print("="*40)
        print(Fore.BLUE + Style.BRIGHT + "              Game End")
        print("="*40)
        break
    

