from collections import deque,defaultdict

class CurrencyConverter:
    def __init__(self,arr):
        self.dic = defaultdict(list)
        for i in arr:
            self.dic[i[0]].append((i[1],i[2]))
        print(self.dic)

    def ConvertCurrency(self,cur1,cur2,graph):
        visited = []
        q = deque([(cur1,1.0)])
        while q:
            
            currency,val = q.popleft()
            if currency not in visited:
                visited.append(currency)
                
            if currency == cur2:
                return val
            

            for i in graph[currency]:
                currencyChild,valChild = i
                if currencyChild not in visited:
                    valChild = val * valChild
                    q.append((currencyChild,valChild))

arr = [["USD","INR", 80],["INR","AUD",0.4],["INR","ZEN",0.5],["ZEN","PINR",0.7]]
c = CurrencyConverter(arr)
print(c.ConvertCurrency("USD","PINR",c.dic))