class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k

    # Count the frequency of each remainder when divided by k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

    # Check if we can form valid pairs
        for r in range(1, k):
            if remainder_count[r] != remainder_count[k - r]:
                return False

    # Special case for remainder 0, must be even
        return remainder_count[0] % 2 == 0
        