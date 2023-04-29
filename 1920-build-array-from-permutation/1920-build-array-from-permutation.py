class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        vec = [0]*len(nums)
        for i in range(0, len(nums)):
            vec[i] = nums[nums[i]]
        return vec
        