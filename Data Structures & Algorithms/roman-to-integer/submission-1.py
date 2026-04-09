class Solution(object):
    def romanToInt(self, s):
        conversionMap = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        integerValue = 0

        for i in range(len(s)):
            # if next char exists and is bigger, subtract current
            if i + 1 < len(s) and conversionMap[s[i]] < conversionMap[s[i+1]]:
                integerValue -= conversionMap[s[i]]
            else:
                integerValue += conversionMap[s[i]]

        return integerValue