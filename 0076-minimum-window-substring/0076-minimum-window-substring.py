class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        left = 0
        required = len(t)
        formed = 0

        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]
            if char in freq:
                if freq[char] > 0:
                    formed += 1
                freq[char] -= 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                if left_char in freq:
                    freq[left_char] += 1
                    if freq[left_char] > 0:
                        formed -= 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]