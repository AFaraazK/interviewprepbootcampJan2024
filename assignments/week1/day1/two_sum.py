from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapN = {}
        lenN = len(nums)

        for i in range (lenN):
            pair = target - nums[i]
            if pair in mapN:
                return [mapN[pair], i]
            mapN[nums[i]] = i
        return []