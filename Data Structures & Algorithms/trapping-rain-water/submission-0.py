class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        leftval,rightval = height[left],height[right]
        water = 0
        while left < right:
            if leftval < rightval:
                left +=1
                leftval = max(leftval,height[left])
                water += leftval - height[left]
            else:
                right -=1
                rightval = max(rightval,height[right])
                water += rightval - height[right]
        return water
