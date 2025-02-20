class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return None
        
        dp = [False for i in range(len(s)+1)]
        m = len(dp)
        dataStore = set(wordDict)
        dp[0] = True
        
        for i in range(1, m):
            for j in range(0,i):
                if dp[j] == True and s[j:i] in dataStore:
                    dp[i] = True
                    break
        
        return dp[len(dp)-1]
        
