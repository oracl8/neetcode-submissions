class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        org = "".join(sorted(s1))
        for r in range(len(s1),len(s2)+1):
            new = "".join(sorted(s2[l:r])) 
            if new == org:
                return True
            l+=1
        return False