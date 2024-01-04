from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map1 = {}

        for i,n in enumerate(numbers):
            complement = target - n
            if complement in map1:
                return [map1[complement] + 1, i + 1]
            map1[n] = i
