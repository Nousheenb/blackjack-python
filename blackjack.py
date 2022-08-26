#blacjack project
import os
import art
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
com_cards=[]
def user():
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    f_score=0
    for i in user_cards:
        f_score+=i
    print(f"Your cards are : {user_cards} , current score is {f_score}")
def user_final_score():
    final_score=0
    for x in user_cards:
        final_score+=x
    return final_score
def computer_final_score():
    com_cards.append(first_card)
    com_cards.append(random.choice(com_cards))
    score=0
    for x in user_cards:
        score+=x
    return score
def result():
    if final_score==score:
        print("it's a draw")
    elif final_score>21:
        print("You are score is greater than 21 , You loose")
    elif score>21:
        print("You won")
    elif final_score<score:
        print("you went over , You lose")
    else :
        print("You won")
con=input("Do you want to play blackjack game(y/n)? ")
if con=="y":
    os.system('clear')
    print(art.logo)
    user()
    first_card=random.choice(cards)
    print(f"Computer's first card: {first_card}")
    con2=input("Type 'y' to get another card, type 'n' to pass:")
    if con2=='y':
        user_cards.append(random.choice(cards))
        final_score=user_final_score()
        score=computer_final_score()
        print(f"your final hand : {user_cards} , final score : {final_score}")
        print(f"computer's final hand : {com_cards} , final score : {score}")
        result()
    else:
        final_score=user_final_score()
        score=computer_final_score()
        print(f"your final hand : {user_cards} , final score : {final_score}")
        print(f"computer's final hand : {com_cards} , final score : {score}")
        result()
        
  
