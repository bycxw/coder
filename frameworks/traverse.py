# coding=utf-8

# 树结构遍历框架
def traverse(root):
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历


# 求二叉树中最大路径和

ans = 0
def one_side_max(root):
    if not root:
        return 0
    left = max(one_side_max(root.left), 0)
    right = max(one_side_max(root.right), 0)
    ans = max(ans, left + right + root.val)
    return max(left, right) + root.val

