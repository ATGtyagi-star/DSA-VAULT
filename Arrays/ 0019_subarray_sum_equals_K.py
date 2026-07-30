class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        count = 0
        currentsum = 0

        for num in nums:
            currentsum += num

            if (currentsum - k) in prefix_map:
                count += prefix_map[currentsum - k]

            prefix_map[currentsum] = prefix_map.get(currentsum,0)+1

        return count 


