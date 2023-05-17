class Solution:
    def trap(self, height) -> int:


        leftMinHeight = 0
        rightMinHeight = 0
        arr = [0] * len(height)
        for i,h in enumerate(height):
            leftMinHeight = max(leftMinHeight,h)
            arr[i] = leftMinHeight
        
        for i,h in reversed(list(enumerate(height))):
            rightMinHeight = max(rightMinHeight,h)
            arr[i] = min(arr[i],rightMinHeight) - height[i]
        
        return sum(arr)