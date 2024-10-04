from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Calculate the total sum of skills
        total_sum = sum(skill)
        n = len(skill)
        
        # If total sum is not divisible by n//2, return -1
        if total_sum % (n // 2) != 0:
            return -1
        
        # The target total skill for each team
        target_skill = total_sum // (n // 2)
        
        # Frequency counter for skills
        skill_count = Counter(skill)
        
        total_chemistry = 0
        
        # Try to form pairs
        for s in skill:
            if skill_count[s] == 0:
                continue  # Skill has already been used in a pair
            
            # Look for the complementary skill needed to form a team with skill s
            complement = target_skill - s
            
            if skill_count[complement] > 0:
                # Found a valid pair (s, complement)
                total_chemistry += s * complement
                
                # Decrease the count of both the skill and its complement
                skill_count[s] -= 1
                skill_count[complement] -= 1
            else:
                # No valid pair found, return -1
                return -1
        
        return total_chemistry

        