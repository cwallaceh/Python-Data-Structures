# Implementing a Trie using a dictionary in Python

#      t
#    /   \
#   h     e
#    \   / \
#     e a   n


class Trie():

    def __init__(self):
        self.trie = dict()

    def __repr__(self):
        return "Trie(%s)" % self.trie

    def insert(self, word):
        if self.find(word):
            pass
        else:
            trie = self.trie

            temp_dict = trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})

            self.trie = trie

    def find(self, word):
        temp_dict = self.trie

        for letter in word:
            if letter in temp_dict.keys():
                temp_dict = temp_dict[letter]
            else:
                return False

        return True


trie = Trie()
print(trie)
trie.insert('tea')
trie.insert('the')
trie.insert('ten')
print(trie)
print(trie.find('ten'))
