from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for s in strs:
            map1["".join(sorted(s))].append(s)
        return map1.values()