class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        print(n)
        x = n.count('1')
        print(x)
        return x
        