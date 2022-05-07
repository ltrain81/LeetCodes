class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        standard = self.AllSub(strs[0])
        longest = ""
        
        standard.reverse()
        
        #print(standard)
        
        for cand in standard:
            cnt = 0
            n = len(cand)
            for str in strs:
                if cand != str[0:n]:
                    print(str[0:n])
                    break
                else:
                    cnt += 1
            
            if cnt == len(strs):
                longest = cand
                break
        
        return longest
            
    
    def AllSub(self, x):
        result = [x[0:j] for j in range(1, len(x) + 1)]
        return result