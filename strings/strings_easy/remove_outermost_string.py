from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        # TC : O(N)  , SC : O(N)
        result = []
        counter = 0

        for c in s:
            if c == '(':
                if counter > 0:
                    result.append(c)
                counter +=1 
            else:
                counter -= 1
                if counter > 0:
                    result.append(c)

        return ''.join(result)


if __name__ == '__main__':
    
    S = Solution()

    s = "(()())(())"
    print(S.removeOuterParentheses(s))

    s = "(()())(())(()(()))"
    print(S.removeOuterParentheses(s))

    s = "()()"
    print(S.removeOuterParentheses(s))


            
