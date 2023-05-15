class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            menor = min(strs, key=len)
            sol = ""
            for i in range(len(menor)):
                for char in strs:
                    if char[i] != strs[0][i]:
                        return sol
                sol += strs[0][i]
            return sol
