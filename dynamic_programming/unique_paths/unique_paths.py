class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom up DP Tabulation
        # build dp table with all 0s
        dp = []
        for i in range(m):
            dp.append([0] * n)

        # start position is base case = 1
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                # skip start position
                if i == 0 and j == 0:
                    continue

                val = 0

                if i > 0:
                    val += dp[i - 1][j]

                if j > 0:
                    val += dp[i][j - 1]

                dp[i][j] = val

        return dp[m - 1][n - 1]

    # Time: O(m * n)
    # Space: O(m * n)
