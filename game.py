import random
from art import logo,vs
from gamedata import data
def random_generator():
    random_A =random.choice(data)
    return random_A   
def game():
    gameshouldcontinue = True
    A =random_generator()
    B =random_generator()
    score =0
    print("Working")
    while gameshouldcontinue==True:
        A =B
        B=random_generator()
        a_count =A.get("follower_count")
        a_name =A.get("name")
        a_desc =A.get("description")
        a_country =A.get("country")
        B =random_generator()
        b_count =B.get("follower_count")
        b_name =B.get("name")
        b_desc =B.get("description")
        b_country =B.get("country")
        print(logo)
        print("Welcome to the Higher-Lower Game")
        print(f"Today we are comparing {a_name},a {a_desc} from {a_country} and {b_name} ,a {b_desc} from {b_country}")
        print(vs)
        user_inp =input("Choose A or B: ")
        if user_inp=="a":
            if a_count>b_count:
                score+=1
                print(f"Your current score is {score}")
            else:
                gameshouldcontinue=False
                print("You Lose")
                print(f"Your Score was {score}")
        elif user_inp=="b":
            if b_count>a_count:
                score+=1
                print(f"Your current score is {score}")
            else:
                gameshouldcontinue=False
                print("You Lose")
                print(f"Your Score was {score}")
        else:
            print("You Lose")  
game()                          

    