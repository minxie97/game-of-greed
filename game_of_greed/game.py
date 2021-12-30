from sys import exit
from game_of_greed.game_logic import GameLogic

roller = GameLogic.roll_dice

welcome_intro = '''Welcome to Game of Greed
(y)es to play or (n)o to decline
> '''


class Game:
    def __init__(self):
        pass

    def play(self, roller):
        choice = input(welcome_intro)

        if choice.lower() in ['n', 'no']:
            print('OK. Maybe another time')
            exit()












if __name__ == '__main__':
    game = Game()
    game.play(roller)