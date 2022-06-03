class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        b= [] 
        for i in sentence :
            if i not in b :
                b.append(i)
        if len(b) == 26 :
            return True
        else :
            return False
        
        
        # return len(set(sentence)) == 26 %
        