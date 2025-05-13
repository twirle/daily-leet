# A string can be shortened by replacing any number of non-adjacent, non-empty substrings with their lengths (without leading zeros).

# For example, the string "implementation" can be abbreviated in several ways, such as:
#     "i12n" -> ("i mplementatio n")
#     "imp4n5n" -> ("imp leme n tatio n")
#     "14" -> ("implementation")
#     "implemetation" -> (no substrings replaced)

# Invalid abbreviations include:
#     "i57n" -> (i mplem entatio n, adjacent substrings are replaced.)
#     "i012n" -> (has leading zeros)
#     "i0mplementation" (replaces an empty substring)

# You are given a string named word and an abbreviation named abbr, return true if abbr correctly abbreviates word, otherwise return false.
# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:
# Input: word = "apple", abbr = "a3e"
# Output: true

# Example 2:
# Input: word = "international", abbr = "i9l"
# Output: false

# Example 3:
# Input: word = "abbreviation", abbr = "abbreviation"
# Output: true

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # check between word and abbr
        i = j = 0

        while i < len(word) and j < len(abbr):
            # leading zeros/empty substring case
            if abbr[j] == '0':
                return False

            # matching characters
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1

            # not same alphabets chars
            elif abbr[j].isalpha():
                return False

            # shift both pointers past digit
            else:
                start = j
                # check through how many int digit goes on for, e.g. 2, 12
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                length = int(abbr[start:j])
                i += length

        return i == word, j == abbr

    def __init__(self):
        word = "apple"
        abbr = "a3e"
        result = self.validWordAbbreviation(word, abbr)
        print(result)

        # time complex: o(n) for the size of word and abbr
        # space complex: o(1) nothing stored


solution = Solution()
