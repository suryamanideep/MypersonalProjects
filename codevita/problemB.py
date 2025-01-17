def min_string_factor(X, Y, S, R):
    len_x = len(X)
    len_y = len(Y)
    Y_rev = Y[::-1]  # Reverse of Y
    
    # dp[i] will store the minimum String Factor required to form the first i characters of X
    dp = [float('inf')] * (len_x + 1)
    dp[0] = 0  # Base case, 0 cost for an empty string

    # Iterate over all positions in X
    for i in range(1, len_x + 1):
        # Try all substrings ending at position i-1
        for j in range(max(0, i - len_y), i):  # Ensure we only consider substrings of length <= len_y
            sub_x = X[j:i]  # X[j:i] is the substring of X from j to i-1
            if sub_x == Y:
                dp[i] = min(dp[i], dp[j] + S)
            if sub_x == Y_rev:
                dp[i] = min(dp[i], dp[j] + R)
    
    # Check if we could form the entire string X
    if dp[len_x] == float('inf'):
        return "Impossible"
    
    return dp[len_x]

# Input reading
X = input().strip()
Y = input().strip()
S, R = map(int, input().split())

# Output the result
print(min_string_factor(X, Y, S, R))