class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        if s1_count == s2_count: return True
        L = 0
        for i in range(len(s1), len(s2)):
            # print(s1_count, s2_count)
            s2_count[s2[L]] -= 1
            if s2_count[s2[L]] == 0:
                del s2_count[s2[L]]
            L += 1
            s2_count[s2[i]] += 1
            if s1_count == s2_count: return True

        return False