def findMedianSortedArrays(nums1, nums2) -> float:
    
    nums = nums1+nums2
    nums.sort()
    n = len(nums)
    
    if n%2==0:
        mid =int(n/2) 
        median = (nums[mid]+nums[mid-1])/2
        return median
    else:
        mid = (n-1)/2
        median = int(mid)
        return nums[median]

findMedianSortedArrays([1,3],[3,4])

test = [1,2,3,4]
n = len(test)
print(test)
print("n",n)
print(n//2)
print(test[n//2])

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums3.append(nums1[0])
                nums1 = nums1[1:]
            else:
                nums3.append(nums2[0])
                nums2 = nums2[1:]
        if nums1:
            nums3 += nums1
        if nums2:
            nums3 += nums2
        
        mid = self.getMid(nums3)
        return mid

                
            
       
    
    def getMid(self,num):
        if len(num) == 0:
            return None
        if len(num) == 1:
            m1 =num[0]
        if len(num)%2 == 0:#even
            m = len(num)//2
            mid = (num[m] + num[m-1])/2
            return mid
        else:
            m = len(num)//2
            mid = num[m]
            return mid