class Solution {
public:
    bool isAnagram(string s, string t) {
       /* sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s==t)
        {
            return true;
        }
        else
        {
            return false;
        }
        */
        if (s.size()!=t.size()) return false;
        
		unordered_map <char, int> umap;
        for (char c:s) umap[c]++;
        for(char c:t) {
            umap[c]--;
            
        }
        for(auto it:umap)
        {
            if(it.second) return false;
        }
        
        return true;
                    
    }
    
};