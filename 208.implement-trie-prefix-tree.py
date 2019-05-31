#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = dict()

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        cur = self.tree
        for char in word:
            if char not in cur.keys():
                cur[char] = dict()
            cur = cur[char]
        cur['word']=word

    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        cur = self.tree
        for char in word:
            if char not in cur.keys():
                return False
            cur = cur[char]
        if word == cur.get('word'):
            return True
        else:
            return False

    def startsWith(self, prefix: str):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.tree
        for char in prefix:
            if char not in cur.keys():
                return False
            cur = cur[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

