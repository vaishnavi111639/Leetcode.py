class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        left, right = 0, 0
        n = len(arr)
        maxlen = 0
        zero = 0

        while right < n:
            if arr[right] == 0:
                zero += 1

            if zero > k:
                if arr[left] == 0:
                    zero -= 1
                left += 1

            if zero <= k:
                maxlen = max(maxlen, right - left + 1)

            right += 1

        return maxlen
