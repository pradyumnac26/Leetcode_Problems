class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for key,val in cnt.items() :
            if val >= 2 :
                return key
        