class Solution:
    def maxArea(self, height: List[int]) -> int:

        r=len(height)-1
        l=0
        maxA=0
        while l<r:
            current=(r-l)*min(height[l],height[r])
            maxA=max(current,maxA)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxA