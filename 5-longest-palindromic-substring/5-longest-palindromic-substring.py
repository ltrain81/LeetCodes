class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        front = 0
        left = 0
        right = n-1
        result = ''
        
        #odd case
        for i in range(n):
            #odd
            tmp = self.PalindromeFunc(s, i, i)
            if len(tmp) > len(result):
                result = tmp
                
            #even
            tmp = self.PalindromeFunc(s, i, i + 1)
            if len(tmp) > len(result):
                result = tmp
                
        return result

    def PalindromeFunc(self, s, l, r):
        result = ""
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
                
        