import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "sissor"]

while True:
    user_input = ("Type Rock , Paper , Sissor or q to Quit the game: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = sissors.
    
    computer_pick = options[random_number]
    r = f"Computer Picked {computer_pick}"
    print (r)
    
    if user_input == "rock" and computer_pick == "sissor":
        print("You won")
        user_wins += 1
        
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1
        
    
    elif user_input == "sissor" and computer_pick == "paper":
        print("You won")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1
        
u = f"You won {user_wins} times."
c = f"computer won {computer_wins} times"
print(u)
print(c)
        
print("Goodbye")