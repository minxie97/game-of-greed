from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from sys import exit

class Game:
    def __init__(self):
        self.num_dice = 6
        self.rounds = 1
        self.bank = Banker()
        self.playing = True
        self.current_dice = ''
        self.roller = GameLogic.roll_dice

    def user_roll_dice(self):
        print(f'Rolling {self.num_dice} dice...')
        results = self.roller(self.num_dice)
        self.current_dice = results
        self.print_rolled_dice()

    def print_rolled_dice(self):
        roller_str = ''
        for roll in self.current_dice:
            roller_str += str(roll) + " "
        print(f'*** {roller_str}***')
        
    def user_score(self, response):
        score_tuple = tuple(map(int, list(response)))
        round_score = GameLogic.calculate_score(score_tuple)
        self.bank.shelf(round_score)

    def print_score(self):
        print(f'You have {self.bank.shelved} unbanked points and {self.num_dice} dice remaining')
        # print('(r)oll again, (b)ank your points or (q)uit:')

    def bank_points(self):
        print(f'You banked {self.bank.shelved} points in round {self.rounds}')
        self.rounds += 1
        self.bank.bank()
        print(f'Total score is {self.bank.balance} points')
        self.num_dice = 6
        self.rolled_dice = ''
    
    def end_game(self):
        print(f'Thanks for playing. You earned {self.bank.balance} points.')
        self.playing = False
        exit()

    def player_takes_turn(self):
        self.user_roll_dice()
        isValid = False
        user_input = ''
        while isValid is False:
            print('Enter dice to keep, or (q)uit:')
            user_input = input('> ')
            isValid= self.validate_input(user_input)
            # self.print_rolled_dice()

            if user_input.lower() in ['q', 'quit']:
                self.end_game()

        self.num_dice -= len(user_input)
        self.current_dice = user_input
        self.user_score(user_input)
        self.print_score()

    def roll_bank_quit(self):
        isValid = False
        user_choice = ''
        while isValid is False:
            user_choice = input('(r)oll again, (b)ank your points or (q)uit: \n> ')
            isValid = self.validate_input(user_choice)
        
        if user_choice.lower() in ['q', 'quit']:
            self.end_game()
        elif user_choice.lower() in ['r', 'roll']:
            self.player_takes_turn
        elif user_choice.locals() in ['b', 'bank']:
            self.bank.bank()


    def validate_input(self, user_input):
        try:
            int(user_input)
            return True
        except Exception as e:
            return False

    def play(self):
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

    def game_play(self):
        print(f'Staring round {self.rounds}')
        while self.playing:
            print('game_play loop')
            self.player_takes_turn()


if __name__ == '__main__':
    game = Game()
    game.play()
