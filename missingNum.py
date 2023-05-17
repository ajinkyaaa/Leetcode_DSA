def missingNumber(nums) -> int:
    expected_sum = actual_sum = 0
    print(nums)
    for i, val in enumerate(nums):
        expected_sum += i
        actual_sum += val
    
    return expected_sum + len(nums) - actual_sum

print(missingNumber([0,3,1]))

"""
#steps:-
iterate array and 
calculate sum of index as expected sum
calculate sum of values as actual sum

formula:- 
(sum of index) + len(nums) - actual sum

031

i=0     => i=1      => i=3
sum=0   => sum=3    => sum=4



"""