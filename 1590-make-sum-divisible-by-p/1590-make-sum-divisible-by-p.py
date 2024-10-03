class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        # map remainder of prefix sums to last index
        remain_to_idx = {
            0: -1
        }

        for i, n in enumerate(nums):
            # update current prefix sum modulo p
            cur_sum = (cur_sum + n) % p
            # calculate the target prefix sum to remove
            prefix = (cur_sum - remain + p) % p
            # if the target prefix sum exists in the map, calculate subarray length
            if prefix in remain_to_idx:
                length = i - remain_to_idx[prefix]
                res = min(res, length)
            remain_to_idx[cur_sum] = i

        return -1 if res == len(nums) else res
