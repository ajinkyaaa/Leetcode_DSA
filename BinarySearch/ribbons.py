class Solution:
    def maxLength(self, ribbons, k: int) -> int:


      l =1
      r = min(ribbons)
      curMax = 0
      while l <=r:

        maxRibbon = 0
        m = l+(r-l)//2
       
        for i in ribbons:

          maxRibbon += i//m
        
        if maxRibbon >=k:
          curMax = max(curMax,m)
          l = m+1
        else:
          r = m-1
      print(curMax)
      return curMax
        
s = Solution()
s.maxLength([100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,
100000,

1,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],49)




"""
binary search
range(1,smallestVal+1) => 1,5

val = 3
step1:-  3 + 2 + 1 > k
          l = m+1
          sum < k
          r = m-1



"""