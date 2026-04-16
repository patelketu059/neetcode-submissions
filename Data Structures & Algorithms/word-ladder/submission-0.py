class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        graph = defaultdict(list)
        length = len(beginWord)
        pattern = defaultdict(list)
        for word in wordList:
            for i in range(length):
                p = tuple([word[:i], word[i + 1:]])
                pattern[p].append(word)


        for p in pattern.values():
            for word in range(len(p)):
                for word2 in range(word, len(p)):
                    if p[word] != p[word2]:
                        graph[str(p[word])].append(str(p[word2]))
                        graph[str(p[word2])].append(str(p[word]))
        q = deque()
        q.append(beginWord)
        res = 0
        seen = set()
        while q and len(seen) < len(wordList): 
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                seen.add(node)
                if node == endWord:
                    return res
                for nei in graph[node]:
                    if nei not in seen:
                        q.append(nei)

        return 0


