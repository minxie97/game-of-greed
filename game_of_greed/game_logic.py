import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
    
    @staticmethod
    def calculate_score(dice_tuple):
        pass


