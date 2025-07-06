class Solution:
    def isIsomorphic(self, s:str, t:str)->bool:
        if len(s)!=len(t) or len(s) == 0:
            return False
        hashST,hashTS = {},{}
        for c1,c2 in zip(s,t):
            if (c1 in hashST and hashST[c1] != c2) or (c2 in hashTS and hashTS[c2]!= c1):
                return False
            hashST[c1] = c2
            hashTS[c2] = c1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "egg"
    t = "add"
    print(sol.isIsomorphic(s, t))

    s = "foo"
    t = "bar"
    print(sol.isIsomorphic(s, t)) 

    s = "abc"
    t = "dee"
    print(sol.isIsomorphic(s, t)) 
    




    