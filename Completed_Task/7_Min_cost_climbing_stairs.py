class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        # Step 1: create dp array
        dp = [0] * n

        # Step 2: base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Step 3: fill dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # Step 4: result (top can be reached from last or second last step)
        return min(dp[n - 1], dp[n - 2])