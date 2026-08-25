class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom up - Time O(n) ; Space O(n)
        # n = len(cost)
        # dp = [0] * (n+1)
        
        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[n]

        # Bottom up - Time O(n) ; Space O(1)

        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
        return min(cost[0],cost[1])