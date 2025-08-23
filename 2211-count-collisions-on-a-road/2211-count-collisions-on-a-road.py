class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        lastPushed = None
        collisions = 0

        for direction in directions :
            while (lastPushed == 'R' and (direction == 'S' or direction == 'L')) or  (lastPushed == 'S' and  direction == 'L') :
                stack.pop()

                if (direction == 'L' and lastPushed == 'R') :
                    collisions += 2
                else :
                    collisions += 1

                direction = "S"
                if len(stack) > 0 :
                    lastPushed = stack[-1]
                else :
                    lastPushed = None

            stack.append(direction)
            lastPushed = direction


        return collisions