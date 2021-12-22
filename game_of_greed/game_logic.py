import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        dice_list = []
        for _ in range(num_dice):
            dice_list.append(random.randint(1, 6))
        return tuple(dice_list)
    
    @staticmethod
    def calculate_score(dice_tuple):
        pass