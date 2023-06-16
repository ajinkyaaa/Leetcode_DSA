class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


"""

tbl1:-

name age phn    
a     1   212
c     1   212

tbl2:-

name age phn  
a     1   212
b     1   212

select * from tbl1 inner join tbl2 on tbl1.name = tbl2.name and tbl1.age = tbl2.age and tbl1.phn - tbl2.phn


"""