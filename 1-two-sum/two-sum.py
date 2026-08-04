class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in mp:
                return [mp[com],i]
            else:
                mp[nums[i]]=i
        