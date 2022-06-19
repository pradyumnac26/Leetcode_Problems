class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x > sum(nums):
            return -1
        elif x == sum(nums):
            return len(nums)
        
        target = sum(nums) - x # "new" target
        longest = 0 # track the longest subarray sum equals target
        preSum = 0 # prefix sum
        hashMap = {} # hash map (prefix sum: index) 
        
        for i, n in enumerate(nums):
            preSum += n
            
            # generate a hash map preSum -> i
            if preSum not in hashMap:
                hashMap[preSum] = i
            
            # when subarray sum equals target
            if preSum == target:
                longest = max(longest, i + 1)
            
            # when the difference between prefix sum and target is another prefix sum
            diff = preSum - target
            if diff in hashMap:
                longest = max(longest, i - hashMap.get(diff))
            
        if longest == 0: # corner case: NO subarray sum equals target
            return -1
        else:
            return len(nums) - longest


                
            
            
            
            
        