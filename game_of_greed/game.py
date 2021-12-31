from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from sys import exit

class Game:
    def __init__(self):
        self.num_dice = 6
        self.rounds = 1
        self.bank = Banker()
        self.playing = True

    def user_roll_dice(self):
        results = self.roller(self.num_dice)
        roller_str = ''
        print(f'Rolling {self.num_dice} dice...')
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

    def bank_points(self):
        print(f'You banked {self.bank.shelved} points in round {self.rounds}')
        self.rounds += 1
        self.bank.bank()
        print(f'Total score is {self.bank.balance} points')
        self.num_dice = 6
    
    def end_game(self):
        print(f'Thanks for playing. You earned {self.bank.balance} points.')
        exit()

    def player_choice(self):
        valid_input = None
        while valid_input not in []:
            print('Enter dice to keep, or (q)uit:')
            valid_input = input('> ')

    def play(self, roller = GameLogic.roll_dice):
        self.roller = roller
        yes_or_no = None
        print('Welcome to Game of Greed')
        while yes_or_no not in ['y', 'yes']:
            print('(y)es to play or (n)o to decline')
            yes_or_no = input('> ')

            if yes_or_no.lower() in ['n', 'no']:
                print('OK. Maybe another time')
                exit()
            elif yes_or_no.lower() in ['y', 'yes']:
                self.game_play()
            else:
                print('You must choose....but choose wisely')

    def play_round(self):
        user_input = ''
        print(f'Staring round {self.rounds}')
        self.user_roll_dice()
        print('Enter dice to keep, or (q)uit:')
        user_input = input('> ')








    def game_play(self):
        while self.playing:
            self.play_round()
        self.end_game()








if __name__ == '__main__':
    game = Game()
    game.play()






# class Game:

#     def __init__(self):
#         self.num_dice = 6
#         self.rounds = 1
#         self.bank = Banker()
#         self.playing = True
    
#     def play(self, roller = GameLogic.roll_dice):
#         self.roller = roller
#         print('Welcome to Game of Greed')
#         print('(y)es to play or (n)o to decline')

#         yes_or_no = input('> ')

#         if yes_or_no.lower() in ['n', 'no']:
#             print('OK. Maybe another time')
#             exit()
#         else:
#             self.game_start()

#     def user_roll_dice(self):
#         print(f'Rolling {self.num_dice} dice...')
#         results = self.roller(self.num_dice)
#         self.print_dice_rolls(results)

#     def print_dice_rolls(self, results):
#         roller_str = ''
#         for roll in results:
#             roller_str += str(roll) + " "
#         print(f'*** {roller_str}***')

#     def user_score(self, response):
#         score_tuple = tuple(map(int, list(response)))
#         round_score = GameLogic.calculate_score(score_tuple)
#         self.bank.shelf(round_score)

#     def print_score(self):
#         print(f'You have {self.bank.shelved} unbanked points and {self.num_dice} dice remaining')
#         print('(r)oll again, (b)ank your points or (q)uit:')

#     def game_start(self):

#         print(f'Starting round {self.rounds}')
#         self.user_roll_dice()

#         while self.playing:
#             print('Enter dice to keep, or (q)uit:')

#             keep_or_quit = input('> ')

#             if keep_or_quit.lower() in ['q', 'quit']:
#                 self.playing = False

#             else: 
#                 self.num_dice -= len(keep_or_quit)
#                 self.user_score(keep_or_quit)
#                 self.print_score()

#                 response = input('> ')
#                 if response.lower() in ['b', 'bank', 'give me money']:
#                     print(f'You banked {self.bank.shelved} points in round {self.rounds}')
#                     self.rounds += 1
#                     self.bank.bank()
#                     print(f'Total score is {self.bank.balance} points')
#                     self.num_dice = 6
#                     print(f'Starting round {self.rounds}')
#                     self.user_roll_dice()

#                 elif response.lower() == 'r':
#                     self.user_roll_dice()

#                 elif response.lower() in ['q', 'quit']:
#                     self.playing = False

#         print(f'Thanks for playing. You earned {self.bank.balance} points')
#         exit()


# if __name__ == '__main__':
#     game = Game()
#     game.play()

