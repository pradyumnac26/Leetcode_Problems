class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i =0 
        j =len(numbers) -1 
        b = []
        while i<j :
            s = numbers[i] + numbers[j]
            if s == target :
                b.append(i+1)
                b.append(j+1)
        
            if s > target :
                j = j-1
            else : 
                i = i+1
                
        return b