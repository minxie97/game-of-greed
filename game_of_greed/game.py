try:
    from game_of_greed.game_logic import GameLogic
    from game_of_greed.banker import Banker  
except:
    from game_logic import GameLogic
    from banker import Banker  
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
        return list(results)

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

    def bank_points(self):
        print(f'You banked {self.bank.shelved} points in round {self.rounds}')
        self.rounds += 1
        self.bank.bank()
        print(f'Total score is {self.bank.balance} points')
        self.num_dice = 6
        self.rolled_dice = ''

    def end_game(self):
        print(f'Thanks for playing. You earned {self.bank.balance} points')
        self.playing = False
        exit()

    def play(self, roller=GameLogic.roll_dice):
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
                self.play_game()
            else:
                print('You must choose....but choose wisely')

    def play_game(self):
        print(f'Starting round {self.rounds}')
        dice_rolled = self.user_roll_dice()
        while True:
            self.print_rolled_dice()
            print('Enter dice to keep, or (q)uit:')

            user_input = input('> ')

            if user_input.lower() in ['q', 'quit']:
                self.end_game()
            
            kept_dice = tuple(user_input)
            rolled_dice = tuple(self.current_dice)
            result = GameLogic.validate_keepers(rolled_dice, kept_dice)

            if result == 'q':
                self.end_game()
                
            if result == True:
                self.num_dice -= len(user_input)
                self.current_dice = user_input
                self.user_score(user_input)
                self.print_score()               
                self.continue_round()
            else:
                print('Cheater!!! Or possibly made a typo...')

    # def validate_input(self, user_input, dice_rolled):
    #     if len(user_input) > 6:
    #         return False
    #     try:
    #         int(user_input)
    #         user_list = [int(i) for i in user_input]
    #         check = []
    #         for num in user_list:
    #             if num in dice_rolled:
    #                 check.append(num)

    #             else:
    #                 return False
    #         return True
    #     except ValueError as ve:
    #         if user_input.lower() in ['q', 'quit']:
    #             self.end_game()
    #         return False

    def continue_round(self):
        is_valid_input = False
        while is_valid_input == False:
            print('(r)oll again, (b)ank your points or (q)uit:')
            user_choice = input('> ')
            if user_choice.lower() in ['r', 'roll']:
                self.play_game()
                is_valid_input = True
            elif user_choice in ['b', 'bank']:
                self.bank_points()
                self.play_game()
            elif user_choice in ['q', 'quit']:
                self.end_game()
            else:
                print('Make a fucking choice') 

if __name__ == '__main__':
    game = Game()
    game.play()
