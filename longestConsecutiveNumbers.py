class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest



"""
check start of sequence, check if a consecutive number exists before current number, if false
set length = 1
keep checking if next number exist and increase length by 1
calculate longest length

"""