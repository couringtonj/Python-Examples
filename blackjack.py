import random


def play_game():
    user=[]
    dealer=[]
    dealer_score=-1
    user_score=-1
    for _ in range(2):
        user.append(deal_card())
        dealer.append(deal_card())
    is_game_over=False

    while not is_game_over:
        user_score=calculate_score(user)
        dealer_score=calculate_score(dealer)
        print(f"Your cards: {user}")
        print(f"Dealers cards: {dealer[0]}")
        if user_score==0 or dealer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' for another card, type 'n' to pass: ").lower()
            if user_should_deal=="y":
                user.append(deal_card())
            else:
                is_game_over=True
            
    while dealer_score != 0 and dealer_score<17:
        dealer.append(deal_card())
        dealer_score=calculate_score(dealer)


    print(compare(u_score=user_score,d_score=dealer_score))
    print(f"Your final hand was {user} and the dealers hand was {dealer}")
def deal_card():
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11) and cards.append(1)
        
    return sum(cards)
def  compare(d_score, u_score):
    if d_score==u_score:
        return "Draw"
    elif d_score==0:
        return "Lose, dealer has Blackjack!"
    elif u_score==0:
        return "Win with Blackjack!"
    elif u_score>21:
        return "You went over. You lose"
    elif d_score>21:
        return "Dealer went over, you win!"
    elif u_score>d_score:
        return "You win!"
    else:
        return "You lose"
    



while input("Do you want to play a game of blackjack type 'y' or 'n': ").lower()=='y':
    print("\n"*20)
    play_game()




    
    
