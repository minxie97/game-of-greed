import random
from collections import Counter

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
    
    @staticmethod
    def calculate_score(dice_tuple):
        score = 0
        dice_count = Counter(dice_tuple)
        if len(dice_count) == 6:
            score += 1500
        elif len(dice_count) == 3 and len(set(dice_count.values())) == 1:
            score += 1500
        else:
            for side, count in dice_count.items():
                if count >= 3:
                    score += 1000 * (count - 2) if side == 1 else side * 100 * (count - 2)
                else:
                    if side in [1, 5]:
                        score += 100 * count if side == 1 else 50 * count
        return score
