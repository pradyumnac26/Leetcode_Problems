class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for key,value in cnt.items() :
            if value == 1 :
                return key
        