# Given an array of strings strs, group the
# anagrams
# together. You can return the answer in any order.

# Example 1
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                # e - a = count[4 - 0] = count[4] += 1
                count[ord(char) - ord('a')] += 1

            # turn list of [26] into immutable tuple as key
            # if other strings are anagrams, they will have the same key
            key = tuple(count)
            result[key].append(string)

        return result.values()

    def __init__(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.groupAnagrams(strs)
        print(result)


solution = Solution()
