class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        z = 0
        nums.sort()
        for i in nums :
            z = z + abs(i - nums[len(nums)//2])
        return z

        