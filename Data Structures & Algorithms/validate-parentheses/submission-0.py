class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        openingBraces = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                openingBraces.append(s[i])
            elif s[i] == ')' or s[i] == '}' or s[i] == ']' :
                if not openingBraces:
                        return False

                if  (openingBraces[-1] == '('and s[i] == ')') or \
                    (openingBraces[-1] == '{'and s[i] == '}') or \
                    (openingBraces[-1] == '['and s[i] == ']')  :
                    openingBraces.pop()
                else :
                    return False

        if not openingBraces:
            return True
        else: 
            return False
            

        