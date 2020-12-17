# coding: utf-8
"""
问题的一般形式是求最值
1. 重叠子问题
2. 最优子结构
3. 状态转移方程

明确base case -> 明确状态 -> 明确选择 -> 定义dp数组/函数的含义
"""

# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值:
    for 状态2 in 状态2的所有取值:
        for ...
            dp[状态1][状态2][...] = 求最值(选择1, 选择2, ...)