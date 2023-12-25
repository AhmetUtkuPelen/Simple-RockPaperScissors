import random

def play():
    user=input(" What is your choice ? 'r' for rock , 'p' for paper , 's' for scissors ")
    computer = random.choice(['r','p','s'])

    def win_situation(player,opponent):
        if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
    
    if user == computer:
        return 'tie'
    if win_situation(user,computer):
        return 'win'
    
    return 'lost'

print(play())