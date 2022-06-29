Another approach algorithm : 
Algorithm

1. Store the frequency for each character in the given string s in a frequency array called frequency. We store the frequency for a character c at index c - 'a'. Thus, we will need 26 indices (from 0 to 25) to store the frequencies of the characters.
2. Sort the frequencies (frequency) in descending order.
Set maxFreqAllowed equal to the length of s because this is the maximum frequency a character can have.
3. Iterate over the frequencies in descending order, for each frequency:
4. If frequency[i] > maxFreqAllowed, add the difference of these two in the variable deleteCount. Change frequency of the current character frequency[i] to maxFreqAllowed.
5. Update the maxFreqAllowed to frequency[i] - 1 (or 0 if the value is negative).
6. Return deleteCoun


Used approach algorithm :
1. Store the frequency for each character in the given string s in a frequency array called frequency. We store the frequency for a character c at index c - 'a'. Thus, we will need 26 indices (from 0 to 25) to store the frequencies of the characters.
2. Initialize the variable deleteCount to 0, which stores the count of characters that need to be deleted. Also, initialize a HashSet seenFrequencies that stores the frequencies that have been occupied.
3. Iterate over the characters from a to z as 0 to 25, for each character:
4. Keep decrementing its frequency until it becomes a number that is not present in set seenFrequencies or it becomes zero. Every time we decrement the frequency we increment the variable deleteCount to mark the deletion of the character.
5. When the frequency becomes unique (or zero) insert it into the set seenFrequencies.
6. Return deleteCount.
