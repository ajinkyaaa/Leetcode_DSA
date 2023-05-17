import collections
class Solution:
    def groupAnagrams(self, strs) :
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 90
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            print(tuple(count))
        return ans.values()
s = Solution()
print(s.groupAnagrams(["Yat","tea","tan","ate","nat","bat"]))
#print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

from collections import defaultdict
class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs):
        
        dic = defaultdict(list)
        
        for i in strs:
            dic[tuple(sorted(i))].append(i)
        
  
        return dic.values()
"""
#steps:-
insert tuple sorted in dictionary and append values

"""
print(sorted("bca"))