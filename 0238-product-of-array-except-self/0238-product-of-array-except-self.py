class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        prefix[0] = 1
        b = []
        postfix[len(nums)-1] = 1
        for i in range(1,len(nums)) : 
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1) :
            postfix[i] = postfix[i+1]*nums[i+1]
        for k in range(len(nums)):
            b.append(prefix[k]*postfix[k])
        return b
            
            
            
            