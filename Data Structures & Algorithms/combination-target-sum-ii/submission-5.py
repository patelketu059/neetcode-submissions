class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()

        def backtrack(i, total, subset):
            if total == target: 
                res.add(tuple(subset.copy()))
                return 

            if total > target or i >= len(candidates): return 0

            subset.append(candidates[i])
            backtrack(i + 1, total + candidates[i], subset)
            subset.pop()

            
            backtrack(i + 1, total, subset)

        backtrack(0, 0, [])
        return [list(r) for r in res]