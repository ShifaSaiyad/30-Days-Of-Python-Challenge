class Solution(object):
    def mergeAlternately(self, word1, word2):
        l = []
        i = 0

        # take letters alternately
        while i < len(word1) and i < len(word2):
            l.append(word1[i])
            l.append(word2[i])
            i += 1

        # append remaining letters (if any)
        l.append(word1[i:])
        l.append(word2[i:])

        return "".join(l)


task = Solution()
print(task.mergeAlternately("abc", "pqr"))    # apbqcr
print(task.mergeAlternately("ab", "pqrs"))    # apbqrs
print(task.mergeAlternately("abcd", "pq"))    # apbqcd
