# coding: utf-8

class Trie:
    """recursive Trie Tree"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = dict()
        self.end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            self.end = True
            return
        if word[0] in self.next:
            self.next[word[0]].insert(word[1:])
        else:
            self.next[word[0]] = Trie()
            self.next[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return self.end
        if word[0] in self.next:
            return self.next[word[0]].search(word[1:])
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        if prefix[0] in self.next:
            return self.next[prefix[0]].startsWith(prefix[1:])
        else:
            return False


class Trie2:
    """iterative Trie Tree"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.end = "end"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for c in word:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                cur_node[c] = dict()
                cur_node = cur_node[c]
        cur_node[self.end] = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for c in word:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False
        return cur_node.get(self.end, False)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for c in prefix:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)