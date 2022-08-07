def longestIdealString(s: str, k: int) -> int:
    res = []
    n = len(s)

    def dfs(l, a, m):
        res.append(l)
        if a == n:
            return
        for i in range(a, n):
            if not m or abs(ord(m[-1]) - ord(s[i])) <= k:
                dfs(l + 1, a + 1, m + s[i])

    dfs(0, 0, '')
    return res
a = longestIdealString("acfgbd",2)
print(a)