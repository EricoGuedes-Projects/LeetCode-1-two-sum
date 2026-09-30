from typing import List

# Time complexity: O(n) where n == len(nums)
# Space complexity: O(n) where n == len(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup and i != lookup[complement]:
                return [lookup[complement], i]
