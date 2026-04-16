class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookUp = defaultdict(list)
        for word in strs:
            c = [0] * 26
            for l in word:
                c[ord(l) - ord('a')] += 1
            lookUp[str(c)].append(word)


        return [v for k,v in lookUp.items()]