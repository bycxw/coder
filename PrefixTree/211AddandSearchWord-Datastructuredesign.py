# coding: utf-8
# https://leetcode.com/problems/add-and-search-word-data-structure-design/


class WordDictionary:
    """recursive implement, trie tree"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = dict()
        self.end = False
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not word:
            self.end = True
            return
        if word[0] in self.next:
            return self.next[word[0]].addWord(word[1:])
        else:
            self.next[word[0]] = WordDictionary()
            self.next[word[0]].addWord(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return self.end
        if word[0] != '.':
            if word[0] in self.next:
                return self.next[word[0]].search(word[1:])
            else:
                return False
        else:
            for _, value in self.next.items():
                if value.search(word[1:]):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)