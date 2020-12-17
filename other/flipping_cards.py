# coding: utf-8

# the optimal stopping time

# there are 52 cards, 26 reds and 26 blacks. turn over a card. you'll get 1 yuan if it's red. Otherwise
# lose 1 yuan. Find a strategy to maximize profit.

def max_profit(n):
    # define value function dp[red][black] expected payoff, red and black is the cards without turnoff
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(0, i / (i + j) * (1 + dp[i - 1][j]) + j / (i + j) * (-1 + dp[i][j - 1]))
    print(dp[n][n])

if __name__ == '__main__':
    max_profit(26)