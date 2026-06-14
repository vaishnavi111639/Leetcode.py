class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur = 0
        direction = -1

        for ch in s:
            rows[cur] += ch

            if cur == 0 or cur == numRows - 1:
                direction *= -1

            cur += direction

        return "".join(rows)