from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map1 = {}
        for i in nums:
            if i in map1:
                return True
            else:
                map1[i] = True
        return False
