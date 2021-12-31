from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from sys import exit

class Game:

    def __init__(self):
        self.num_dice = 6
        self.rounds = 1
        self.bank = Banker()
        self.playing = True
    
    def play(self, roller = GameLogic.roll_dice):
        self.roller = roller
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')

        yes_or_no = input('> ')

        if yes_or_no.lower() in ['n', 'no']:
            print('OK. Maybe another time')
            exit()
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

    def print_score(self):
        print(f'You have {self.bank.shelved} unbanked points and {self.num_dice} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')

    def game_start(self):

        while self.playing:
            print(f'Starting round {self.rounds}')
            self.user_roll_dice()
            print('Enter dice to keep, or (q)uit:')

            keep_or_quit = input('> ')

            if keep_or_quit.lower() in ['q', 'quit']:
                self.playing = False
       
            else: 
                self.num_dice -= len(keep_or_quit)
                self.user_score(keep_or_quit)
                self.print_score()

                response = input('> ')
                if response.lower() in ['b', 'bank', 'give me money']:
                    print(f'You banked {self.bank.shelved} points in round {self.rounds}')
                    self.rounds += 1
                    self.bank.bank()
                    print(f'Total score is {self.bank.balance} points')
                    self.num_dice = 6

                elif response.lower() in ['q', 'quit']:
                    self.playing = False

                elif response.lower() == 'r':
                    print('Doing R stuff')
                    
        print(f'Thanks for playing. You earned {self.bank.balance} points')
        exit()


if __name__ == '__main__':
    game = Game()
    game.play()
    