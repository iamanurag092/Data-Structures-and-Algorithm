class Solution:
    def maxArea(self, height: List[int]) -> int:

        r = len(height) - 1
        l = 0
        max_area = 0

        while l < r:

            current_area = (r - l) * min(height[l], height[r])

            max_area = max(max_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area