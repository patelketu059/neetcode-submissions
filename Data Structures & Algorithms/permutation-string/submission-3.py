class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for ch in range(len(s1)):
            s1_count[ord(s1[ch]) - ord('a')] += 1
            s2_count[ord(s2[ch]) - ord('a')] += 1
        
        if tuple(s1_count) == tuple(s2_count): return True
        # s1_count = set(tuple(s1_count))
        # print(s1_count)
        # print(s2_count)
        # print("****")
        L = 0
        for R in range(len(s1), len(s2)):

            # print(s1_count)
            s2_count[ord(s2[L]) - ord('a')] -= 1
            s2_count[ord(s2[R]) - ord('a')] += 1
            L += 1
            if tuple(s1_count) == tuple(s2_count): return True

            # print(s2[R], s2_count)
            
            # print("****")

        return False
