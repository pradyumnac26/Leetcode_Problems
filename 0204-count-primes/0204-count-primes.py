class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while(p*p < n) : 
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
  
    # Print all prime numbers
        cnt = 0 
        for p in range(2, n):
            if prime[p]:
                cnt += 1 
        return cnt
        