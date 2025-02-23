import random
print("Welcome to Rock Paper Sciccors game!!!")
print("0 for Rock, 1 for Paper & 2 for Sciccors")
user=int(input("User Choice: "))
if user>=3 and user<0:
    print("Enter valid number")
else:
    com=random.randint(0,2)
    print(f"Computer choice: {com}")
    if com==user:
        print("Game is Draw")
    elif com>user:
        print("You lose.")
    elif user>com:
        print("You Win")
    elif com == 0 and user ==2:
        print("You lose")
    elif user==0 and com==2:
        print("You win")
    
