class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort( reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

"""
set position and speed tuple
sort them in reverse order of position
calculate time for each of them to reach target and append to stack
if last item requires less time then merge both and pop stack
"""