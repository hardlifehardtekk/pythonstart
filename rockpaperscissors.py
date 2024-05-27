import random


def choice():
    user = input("'r' for rock 's' for scissors 'p' for paper")
    comp = random.choice(['r','p','s'])
    if user == comp:
        return True
    if is_win(user,comp):
        return 'You win'
    return 'You lose'

def is_win(player, opp):
    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') \
    or (player == 'p' and opp == 'r'):
        return True

    