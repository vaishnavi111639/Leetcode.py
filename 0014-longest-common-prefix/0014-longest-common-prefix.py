class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        pref_len = len(pref)
        for i in strs[1:]:
            while pref != i[0:pref_len]:
                pref_len -= 1
                pref = pref[:pref_len]
                if pref_len == 0:
                    return ""
        return pref


        