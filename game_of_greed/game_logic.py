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
    
    @staticmethod
    def dice_tuple_to_dict(tup):
        result_dict = {}
        for i in list(tup):
            if  i in result_dict: 
                result_dict[i] += 1
            else:
                result_dict[i] = 1
        return result_dict

    @staticmethod
    def validate_keepers(roll, keepers):
        rolled = list(roll)
        roll_count = GameLogic.dice_tuple_to_dict(roll)

        try:
            numbers = [int(i) for i in list(keepers)]

            if len(numbers) > len(rolled):
                return False

            for num in numbers:
                num_count = numbers.count(num)
                print(num_count)
                if num_count > roll_count[num]:
                    return False
            return True

        except Exception as e:
            return False

if __name__ == '__main__':
    roll = (1,2, 5, 5,)
    keepers = (1,)
    x= GameLogic.validate_keepers(roll, keepers)
    print(x)
