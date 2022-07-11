class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = Counter(s+t)
        print(cnt)
        for key,value in cnt.items() :
            if value%2 != 0 :
                return key
        