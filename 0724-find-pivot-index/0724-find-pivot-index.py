class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        left =0
        for i in range(len(nums)):
            right = totalsum - left - nums[i] 
            if left == right:
                return i
            left += nums[i]

        return -1    
        