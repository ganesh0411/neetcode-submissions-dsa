class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs :
                msg = msg + str(len(s)) + '#' + s 
        return msg


    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0
        while i < len(s):
            # find the # delimiter
            j = i
            while s[j] != '#':
                j += 1
            # read the length
            length = int(s[i:j])
            # extract the string
            result.append(s[j+1 : j+1+length])
            # move i forward
            i = j + 1 + length
        return result