# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

#     The first letter where they differ is smaller in a than in b.
#     There is no index i such that a[i] != b[i] and a.length < b.length.

# Example 1:
# Input: ["z","o"]
# Output: "zo"
# Explanation:
# From "z" and "o", we know 'z' < 'o', so return "zo".

# Example 2:
# Input: ["hrn","hrf","er","enn","rfnn"]
# Output: "hernf"
# Explanation:

#     from "hrn" and "hrf", we know 'n' < 'f'
#     from "hrf" and "er", we know 'h' < 'e'
#     from "er" and "enn", we know get 'r' < 'n'
#     from "enn" and "rfnn" we know 'e'<'r'
#     so one possibile solution is "hernf"

# possible outcomes:
# invalid order: a>b>c but because a>c also, after going a>c, then a>b so a>c>b is an order also
# multiple valid order:
# loop

class Solution(object):
    def foreignDictionary(self, words):
        graph = {character: set() for word in words for character in word}

        # iterate through list of words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # compare between the two words which is shorter
            minLength = min(len(word1), len(word2))

            # same prefix, aka their first x letters are same
            # abcd & abc, but its invalid cus abc should be before abcd
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""

            # check the difference in their character to find the word1>word2 character order
            # abc & abd
            for j in range(minLength):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

            visited = {}
            result = []

        def dfs(character):
            if character in visited:
                return visited[character]

            # visited and in current path
            visited[character] = True

            for neighbour in graph[character]:
                if dfs(neighbour):
                    return True

            # before we return
            visited[character] = False
            result.append(character)

        for character in graph:
            if dfs(character):
                return ""
        result.reverse()
        print("graph", graph)
        return "".join(result)

    def __init__(self):
        words = ["hrn", "hrf", "er", "enn", "rfnn"]
        result = self.foreignDictionary(words)
        print(result)


solution = Solution()
