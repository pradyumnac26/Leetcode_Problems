class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = collections.Counter(nums)
        b = []
        for key,val in x.items() : 
            if val > len(nums)//3 :
                b.append(key)
        return b 