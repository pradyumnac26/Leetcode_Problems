class Solution:
    def minDeletions(self, s: str) -> int:
                # Get the frequency of each character sorted in reverse order
        freq = (list( Counter(s).values()))
        del_count = 0 
        seen_frequencies = set()
        for i in range(len(freq)) :
            while freq[i] and freq[i] in seen_frequencies : 
                freq[i] -=1 
                del_count+=1
            seen_frequencies.add(freq[i])
        return del_count
                
        
