"""
Why is O(1) Space Not Possible for this question in Python :

Strings Are Immutable in Python

TC : O(N)  , SC : O(N)

"""


class Solution:
    def reverseWords(self, s:str) -> str:
        return ' '.join(s.split()[::-1])
    







if __name__ == '__main__' :

    S = Solution()

    s = "the sky is blue"
    print(S.reverseWords(s))

    s = "  hello world  "
    print(S.reverseWords(s))

    s = "a good   example"
    print(S.reverseWords(s))
