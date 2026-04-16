class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '.!@#'
        for i in strs:
            res = res + str(len(i)) + "@@@@@" + i
        return res + ".!@#"

    def decode(self, s: str) -> List[str]:
        res = []
        s = s[4:]
        s = s[:-4]
        i = 0
        # print(s)
        while i < len(s):
            R = i
            while s[R] != '@':
                R += 1
            length = int(s[i:R])
            i = R + 5
            R = i + length
            
            res.append(s[i:R])
            print(res)
            i = R

        
        return res
