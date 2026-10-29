class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i in range(0,len(nums)):
            element=target-nums[i]
            if element in track:
                return [track[element], i]
            track[nums[i]]=i

