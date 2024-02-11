class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate_num = sum(nums) - sum(set(nums))
        expected_sum = sum(range(1, len(nums) + 1))
        actual_sum = sum(set(nums))
        missing_num = expected_sum - actual_sum

        return [duplicate_num, missing_num]
            
            
        