# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def addWord(self, word):
        if word:
            self.set.add(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            if word in self.set:
                return True
            else:
                return False
        # Tip: how to implement wildcard
        for w in self.set:
            for i in range(len(word)):
                # compare each char in word with each element in set, '.' allow pass
                if word[i] != w[i] and word[i] != '.':
                    break
            # "for...else..." loop fell through without finding a factor
            else:
                return True

        return False


class TrieNode(object):
    def __init__(self, char):
        self.val = char
        self.children = {}
        self.isWord = False


class WordDictionary2(object):

    def __init__(self):
        self.root = TrieNode(0)

    def addWord(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                newNode = TrieNode(w)
                node.children[w] = newNode
                node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root

        def dfs(node, word, i):
            if i == len(word):
                return False
            if i == len(word) - 1 and node.isWord:
                return True
            elif i == len(word) - 1 and not node.isWord:
                return False
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                else:
                    dfs(node.children[word[i]], word, i + 1)
            else:
                if node.val != word[i]:
                    return False
                for v in node.children.values():
                    dfs(v, word, i + 1)

        # Bug, forgot to check '.' at first letter
        if word[0] not in node.children:
            return False
        else:
            return dfs(node.children[word[0]], word, 0)

obj = WordDictionary2()
obj.addWord("word")
obj.addWord("work")
obj.addWord("wolf")
print obj.search(".ord")
print obj.search("w.rd")