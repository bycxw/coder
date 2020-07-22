# coding: utf-8
# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

NULL_SYB = 'null'
SEP = ','

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        Preorder traverse with null ptr.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        self.stream = []
        self.preorder(root)
        return SEP.join(self.stream)

    def preorder(self, root):
        if not root:
            self.stream.append(NULL_SYB)
            return
        self.stream.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Decodes from preorder traverse stream.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        flag, num, stream = self.read_stream(data)
        root = None
        if flag:
            root = TreeNode(num)
            root.left, stream = self.deserialize_core(stream)
            root.right, stream = self.deserialize_core(stream)
        return root

    def deserialize_core(self, stream):
        if not stream:
            return None, None
        flag, num, stream = self.read_stream(stream)
        root = None
        if flag:
            root = TreeNode(num)
            root.left, stream = self.deserialize_core(stream)
            root.right, stream = self.deserialize_core(stream)
        return root, stream

    def read_stream(self, stream):
        if not stream:
            raise Exception("Invalid input stream.")
        stream = stream.split(SEP, 1)
        try:
            num = int(stream[0])
            flag = True
        except:
            num = stream[0]
            flag = False

        if len(stream) > 1:
            stream = stream[1]
        else:
            stream = ""
        return flag, num, stream

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

codec = Codec()
codec.deserialize("-1,0,null,null,1,null,null")