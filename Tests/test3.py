"""
2: [a,b,c],
3: [d,e,f],
4: [g,h,i],
5: [j,k,l],
6: [m,n,o],
7: [p,q,r,s],
8: [t,u,v],
9: [w,x,y,z]



23 => ad ae af bd be bf cd ce cf
2 => a b c
3 => d e f


"""

def getPhoneLetter(inp):
    dic = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }

    
        
    def backtrack(inp,path):
        if len(inp) == 0:
            print("".join(path))
            return
        else:
            
            for c in dic[inp[0]]:
                backtrack(inp[1:],path + [c])
    backtrack(inp,[])

getPhoneLetter("253")
