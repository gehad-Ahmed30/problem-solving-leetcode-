from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        output={}
        for i,num in enumerate(nums):
            if num in output and i-output[num]<=k:
                return True
            output[num]=i
        return False
