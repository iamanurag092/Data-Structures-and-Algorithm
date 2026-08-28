# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(0,len(nums)):
#             nums[i]*=nums[i]
#         nums.sort()
#         return nums

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):

            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result