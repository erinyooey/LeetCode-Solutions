class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in frequency:
                frequency[s[i]] = 0
            if t[i] not in frequency:
                frequency[t[i]] = 0

            frequency[s[i]] += 1
            frequency[t[i]] -= 1

        for key in frequency:
            if frequency[key] != 0:
                return False
        return True
