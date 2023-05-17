grid = [["o","r","b","s"],
       ["e","a","a","e"],
       ["i","a","a","r"],
       ["i","f","l","v"]]

words = ["oath","pea","orbs","aaaa","rbs","aaar"]

class Trie:
    def __init__(self,char):
        self.char = char
        self.child = {}
        self.wordFinished = False

    def add(self,word):
        node = self
        for c in word:
            if c in node.child:
                node = node.child[c]
            else:
                newNode = Trie(c)
                node.child[c] = newNode
                node = node.child[c]
                
        node.wordFinished = True
        return self
c = Trie("*")
c.add("abc")
#

def wordSearch(grid,words):

    ROWS = len(grid)
    COLS = len(grid[0])

    c = Trie("*")
    for word in words:
        c.add(word)
    res = []
    visited = []

    def dfs(row,col,path,n):
        nonlocal ROWS
        nonlocal COLS
        if n.wordFinished == True:
            if "".join(path) not in res:
                res.append("".join(path))
        else:
            char = grid[row][col]
            visited.append(char)
            if  char in n.child:
                if row > 0:
                    dfs(row-1,col,path + [char],n.child[char])
                if row < ROWS-1:
                    dfs(row+1,col,path + [char],n.child[char])
                if col > 0:
                    dfs(row,col-1,path + [char],n.child[char])
                if col < COLS-1:
                    dfs(row,col+1,path + [char],n.child[char])
            visited.pop()
        return

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] in c.child:
                dfs(row,col,[],c)
    return res

print(wordSearch(grid,words))