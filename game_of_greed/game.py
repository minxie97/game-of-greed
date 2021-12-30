from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:

    def __init__(self):
        self.num_dice = 6
        self.rounds = 1
        self.bank = Banker()
    
    def play(self, roller = GameLogic.roll_dice):
        self.roller = roller
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')

        yes_or_no = input('> ')

        if yes_or_no == 'n':
            print('OK. Maybe another time')
        else:
            self.game_start()

    def user_roll_dice(self):
        print(f'Rolling {self.num_dice} dice...')
        results = self.roller(self.num_dice)
        self.print_dice_rolls(results)

    def print_dice_rolls(self, results):
        roller_str = ''
        for roll in results:
            roller_str += str(roll) + " "
        print(f'*** {roller_str}***')

    def user_score(self, response):
        score_tuple = tuple(map(int, list(response)))
        round_score = GameLogic.calculate_score(score_tuple)
        self.bank.shelf(round_score)
        print(f'You have {self.bank.shelved} unbanked points and {self.num_dice} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')

    def game_start(self):
        print(f'Starting round {self.rounds}')
        self.user_roll_dice()
        print('Enter dice to keep, or (q)uit:')

        keep_or_quit = input('> ')

        if keep_or_quit == 'q':
            print('Thanks for playing. You earned 0 points')

        else:
            self.rounds += 1
            self.num_dice -= len(keep_or_quit)
            self.user_score(keep_or_quit)
            response = input('> ')
            if response == 'b':
                self.bank.bank()



