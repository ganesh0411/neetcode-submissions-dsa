class Solution:
    def romanToInt(self, s: str) -> int:
        
        conversionMap  = {}
        conversionMap["I"] = 1
        conversionMap["V"] = 5
        conversionMap["X"] = 10
        conversionMap["L"] = 50
        conversionMap["C"] = 100
        conversionMap["D"] = 500
        conversionMap["M"] = 1000
  
        
        integerValue = 0
        i = 0
        while i < len(s):

            if i + 1 < len(s) and s[i] == 'I' and s[i+1] == 'V':
                integerValue = integerValue + 4
                i = i+2
                continue
            elif i + 1 < len(s) and s[i] == 'I' and s[i+1] == 'X':
                integerValue = integerValue + 9
                i = i+2
                continue
            elif i + 1 < len(s) and s[i] == 'X' and s[i+1] == 'L':
                integerValue = integerValue + 40
                i = i+2
                continue
            elif i + 1 < len(s) and s[i] == 'X' and s[i+1] == 'C':
                integerValue = integerValue + 90
                i = i+2
                continue
            elif i + 1 < len(s) and s[i] == 'C' and s[i+1] == 'D':
                integerValue = integerValue + 400
                i = i+2
                continue
            elif i + 1 < len(s) and s[i] == 'C' and s[i+1] == 'M':
                integerValue = integerValue + 900
                i = i+2
                continue
            else: 
                integerValue = integerValue + conversionMap[s[i]]
                i=i+1

        return integerValue
