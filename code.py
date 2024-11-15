import random
def get_choices():
    player_choice = input("enter a choice (rock,papers,scissors):")
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    choices ={ "player": player_choice, "computer": computer_choice }
    return choices

def diclare_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
      if computer =="scissors":
        return "rock smashes scissors , you won :)"
      else:
         "paper covers rock, you lose"
    elif player == "paper":
      if computer == "rock":
         return "paper covers rock , you won"
      else:
         return "scissors cuts paper, you lose"
    elif player == "scissors": 
      if computer == "paper":
         return "scissors cuts paper , you won"
    else:
       return "rock smashes scissors , you won"
choices = get_choices()
result = diclare_win(choices["player"], choices["computer"])
print(result)
    
