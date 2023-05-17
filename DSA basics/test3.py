
class Trie:
    def __init__(self,char = "*"):
        self.char = char
        self.children = {}
        self.isWordFin = False

    def add(self,wrd):
        n = self

        for c in wrd:
            found = False
            if c in n.children:
                n = n.children[c]
            else:
                newNode = Trie(c)
                n.children[c] = newNode
                n = n.children[c]
        n.isWordFin = True

    def find(self,wrd):
        n = self
        for c in wrd:
            if c in n.children:
                n = n.children[c]
            else:
                return False
        return True

c = Trie()
c.add("cat")
print(c.find("catt"))