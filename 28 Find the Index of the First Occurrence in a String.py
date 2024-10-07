# 28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        # "pepegas" = haystack
        # "gas" = needle
        # 1. if len(needel = 0), return 0
        # 2. check first chars of haystack and needel against each other
        # 3. if it is inside it should be index 4 by the latest since the last few chars are blocked
        # 4. since len(haystack) = 7 and len(needle) = 3

        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            # if haystack[i:i+len(needle)] == needle:
            for index in range(len(needle)):
                if haystack[i+index] != needle[index]:
                    break
                if index == len(needle) - 1:
                    return i
        return -1

        # Knuth Morris Pratt KMP solution
    def strStr2(self, haystack, needle):
        # 'AAACAAAA' = haystack
        # 'AAAA' = needel
        # in this case, it takes more times cus it resets the needle once we reach the wrong X then go back

        if needle == "":
            return 0
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1