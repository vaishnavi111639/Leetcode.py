class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            a = ord(num1[i]) - 48 if i >= 0 else 0
            b = ord(num2[j]) - 48 if j >= 0 else 0

            total = a + b + carry
            carry = total // 10
            result = str(total % 10) + result

            i -= 1
            j -= 1

        return result
