class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left=0
        right=len(height)-1
        water=0

        leftMax=height[left]
        rightMax=height[right]

        while left<right:
            if leftMax<rightMax:
                water+=leftMax-height[left]
                left+=1
                leftMax=max(leftMax,height[left])

            else:
                water+=rightMax-height[right]
                right-=1
                rightMax=max(rightMax,height[right])

        return water



        
        