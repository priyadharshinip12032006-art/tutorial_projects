import random
option = ("rock", "paper", "scissor")
running = True
while running:
    computer = random.choice(option)
    player = None
    while player not in option:
        player = input("enter your choice (rock,paper,scissor): ")
        if player not in option:
            print("Invalid input. Please choose rock, paper, or scissor.")

    print(f"player={player}")
    print(f"computer={computer}")

    if player == computer:
        print("it is a tie")
    elif player == "scissor" and computer == "paper":
        print("you won")
    elif player == "paper" and computer == "rock":
        print("you won")
    elif player == "rock" and computer == "scissor":
        print("you won")
    else:
        print("you lose")
    play_again = input("want to play again (y/n): ")
    if play_again == "n":
        running = False

print("thank you")



