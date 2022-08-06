def maxSumAfterPartitioning(arr, k: int) -> int:
    n = len(arr)
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    if n == 1: return dp[0]
    for i in range(1, n):
        temp_max = 0
        l = 0
        j = i
        while j >= 0:
            l += 1
            if l > k:
                break
            temp_max = max(temp_max, arr[j])
            dp[i] = max(dp[i], dp[j - 1] + temp_max * l)
            j -= 1
    print(dp[-1])

maxSumAfterPartitioning([3,7],2)