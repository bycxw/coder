# coding: utf-8
"""
解决一个回溯问题，实际上是一个决策树的遍历过程。
1. 路径：已经做出的选择
2. 选择列表： 当前可以做的选择
3. 结束条件： 达到决策树底层，无法再做选择的条件
"""

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
