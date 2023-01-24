############### Blackjack  #####################
#DCypher
#01/24/2023
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from replit import clear
from art import logo
import random

""""Returns a random card from the deck"""
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

"""compare user and computer scores to deterine who wins"""  
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose! 😣"
  
  if user_score == computer_score:
    return "Draw! 😒"
  elif computer_score == 0: 
    return "You lose, opponent has Blackjack! 😥"
  elif user_score == 0:
    return "You win with a Blackjack! 😎"
  elif user_score > 21:
    return "You went over. You lose! 😐"
  elif computer_score > 21:
    return "Opponent went over, you win! 😁"
  elif user_score > computer_score:
    return "You Win!! 😍"
  else:
    return "You lose 😣"

"""take a list of cards and return score calculated from the cards"""
def calculate_score(cards):
  #determine if hand contains ace
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #check if ace is worth 1, when deck over 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  #exit calculate_score with sum of cards
  return sum(cards)

  #game start 
def play_game():
  
  print(logo)
  
  #user and computer hands
  user_cards = []
  computer_cards = []
  #flag to track game end
  is_game_over = False
  
  #deal a new card to each hand
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
    #track scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    #interface: Show user his cards and score
    print(f"Your cards: {user_cards}, current score: {user_score}")
    #interface: show computers first card 
    print(f"Computer's first card: {computer_cards[0]}")
   
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
    #allow computer to play after users turn
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
  
    #ask userif he wants to play again
while input("Do you want to play again? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
       
    