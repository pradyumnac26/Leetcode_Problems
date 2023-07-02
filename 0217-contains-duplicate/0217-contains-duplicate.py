class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = collections.Counter(nums)
        print(x.items())
        for key,value in x.items() :
            if value > 1 :
                return True 
            else :
                continue
        return False
        