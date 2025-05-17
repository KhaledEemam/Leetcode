class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        maxNumber , minNumber = max(a,b,c) , min(a,b,c)
        midNumber = 0
        numbers = [a,b,c]
        for number in numbers :
            if number > minNumber and number < maxNumber :
                midNumber = number
        
        if ((maxNumber - midNumber) == 1) and ((midNumber - minNumber) == 1) :
            return [0,0]

        minMoves , maxMoves = 0 , 0

        if ((maxNumber - midNumber) <= 2) or ((midNumber - minNumber) <= 2) :
            minMoves = 1
        else :
            minMoves = 2

        maxMoves = maxNumber - midNumber -1 + midNumber - minNumber - 1

        return [minMoves,maxMoves]