class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for item in nums:
            if item in count:
                return True
            count[item]=1
        return False