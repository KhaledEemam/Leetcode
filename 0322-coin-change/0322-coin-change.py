class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        i = float("inf")
        cur = 0
        steps = 0
        memo = {}

        def get_min_num(cur, steps):
            nonlocal min_steps
            if cur == amount:
                return 0

            if cur > amount:
                return i

            if cur in memo:
                return memo[cur]

            min_steps = i
            for coin in coins:
                min_steps = min(min_steps, 1 + get_min_num(cur + coin, steps + 1))

            memo[cur] = min_steps

            return min_steps

        min_steps = get_min_num(cur, steps)
        return min_steps if min_steps != i else -1