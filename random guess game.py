import random

lower_num=0
highest_num=100
gusses=0
answer=random.randint(lower_num,highest_num)
is_running=True
print("welcome to guesst the number game")
print(f"enter a number bw {lower_num} and {highest_num}")

while is_running:
    guess=int(input("enter your guess: "))
    gusses +=1
    if guess<lower_num or guess>highest_num:
        print("the entered number is out of range")
        print(f" please enter a number bw {lower_num} and {highest_num}")
    elif guess<answer:
        print("enter num is too low")
    elif guess>answer:
        print("enter num is too high")
    else:
        print(f"entered {guess} is correct")
        print(f"no of gusses={gusses}")
        is_running=False




        
