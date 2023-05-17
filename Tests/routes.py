"""
routes = [
    ["DSM","ORD"],
    ["ORD","BGI"],
    ["BGI","LGA"],
    ["SIN","CDG"],
    ["CDG","SIN"],
    ["CDG","BUD"],
    ["DEL","DOH"],
    ["DEL","CDG"],
    ["TLV","DEL"],
    ["EWR","HND"],
    ["HND","ICN"],
    ["HND","JFK"],
    ["ICN","JFK"],
    ["JFK","LGA"],
    ["EYW","LHR"],
    ["LHR","SFO"],
    ["SFO","SAN"],
    ["SFO","DSM"],
    ["SAN","EYW"]


]
STARTING POINT LGA

use case:-
try to reach all destinations
handle circular dependancy
get minimum connections required

1) iterate dic.keys()
2) for each source we do a dfs and add to visited
3) increment count 


                                            DSM                     SIN             DEL<------------------------ TLV            EWR                             EYW   ~
                                          /                        //          /    /  \                                       /                                /     |
                                        ORD                     CDG   -  /              DOH                                 HND                               LHR
                                       /                        /                                                           /  \                              /       |
                                    BGI                      BUD                                                                                            SFO
                                    /                                                                                     INC   JFK                         /   \     |
                                 LGA                                                                                                \                      SAN  DSM
                                                                                                                                    LGA                     |_________|

"""
routes = [
    ["DSM","ORD"],
    ["ORD","BGI"],
    ["BGI","LGA"],
    ["SIN","CDG"],
    ["CDG","SIN"],
    ["CDG","BUD"],
    ["DEL","DOH"],
    ["DEL","CDG"],
    ["TLV","DEL"],
    ["EWR","HND"],
    ["HND","ICN"],
    ["HND","JFK"],
    ["ICN","JFK"],
    ["JFK","LGA"],
    ["EYW","LHR"],
    ["LHR","SFO"],
    ["SFO","SAN"],
    ["SFO","DSM"],
    ["SAN","EYW"]
                                                                           

]

from collections import defaultdict,deque
class Routes:
    def __init__(self,routes):
        self.routes = routes

    def getMinConnections(self):

        dic = defaultdict(list)
        dicOrder = defaultdict(int)
        for val in self.routes:
            dest = val[1]
            src = val[0]
            dicOrder[dest] = 0
            dicOrder[src] = 0

        #print("dicOrder",dicOrder)
        for val in self.routes:
            source = val[0]
            destination = val[1]

            dic[source].append(destination)
            dicOrder[destination] += 1

        #print(dic)
        #print("dicOrder",dicOrder)

        def dfs(n):
            if n in visited:
                return
            else:
                visited.append(n)
                for i in dic[n]:
                    dfs(i)

        q = deque()
        for i in dic.keys():
            for j in dic[i]:
                if j in dic[i]:
                    dicOrder[j] -= 1
                    

        for i in dicOrder.keys():

            if dicOrder[i] == 0:
                q.append(i)


        visited = []
        connectedComponents = 0
        while q and len(visited) < len(dicOrder):
            n = q.popleft()
            if n not in visited:
                connectedComponents += 1
            dfs(n)

            
        
        print("visited" ,visited)
        print(dicOrder.keys())
        return connectedComponents

        
c = Routes(routes)
print(c.getMinConnections())
