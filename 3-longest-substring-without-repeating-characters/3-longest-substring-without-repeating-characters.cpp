class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int res = 0;
        for(int i=0;i<s.size();i++)
        {
            vector<bool>visited(256);
            for(int j=i;j<s.size();j++)
            {
                if(visited[s[j]] == true)
                {
                    break;
                }
                else
                {
                    res = max(res,j-i+1);
                    visited[s[j]] = true; 
                }
            }
        }
        return res;
        
        
    }
};