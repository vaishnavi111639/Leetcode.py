class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        mpp = {}
        maxlen = 0

        for right in range(n):
            if s[right] in mpp and mpp[s[right]] >= left:
                left = mpp[s[right]] + 1

            maxlen = max(maxlen, right - left + 1)
            mpp[s[right]] = right

        return maxlen

        