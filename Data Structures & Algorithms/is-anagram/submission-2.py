class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for item in s:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        
        for item in t:
            if item not in count:
                return False
            count[item] -= 1
        
        for item in s:
            if count[item] != 0:
                return False
        return True