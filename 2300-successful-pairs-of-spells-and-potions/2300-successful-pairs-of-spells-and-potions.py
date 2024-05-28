import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = {}
        potions.sort()
        sorted_spells = sorted(spells , reverse = True)
        index = 0

        for i in range(len(sorted_spells)) :
            spell = sorted_spells[i]
            limit = math.ceil(success / spell)

            while index < len(potions) and limit > potions[index] :
                index += 1

            result[spell] = len(potions) - index

        final_result = []
        for i in spells :
            final_result.append(result[i])

        return final_result