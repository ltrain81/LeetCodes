class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #찾은 중복의 앞까지 날려버리면 된다.
        included = []
        longest = 0
        tracker = 0
                
        for c in s:
            if c not in included:
                tracker += 1
                included.append(c)
            else:
                longest = max(tracker, longest)
                char = included[0]
                cnt = 0
                while char != c:
                    included.pop(cnt)
                    tracker -= 1
                    char = included[0]
                included.remove(c)
                included.append(c)
        
        longest = max(tracker, longest)
        return longest
        