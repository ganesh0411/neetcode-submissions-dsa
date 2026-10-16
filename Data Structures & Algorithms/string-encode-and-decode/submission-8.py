class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedMessage = ""
        for word in strs:
            encodedMessage += str(len(word)) + "#" + word      # length, separator, word
        return encodedMessage

    def decode(self, s: str) -> List[str]:
        decodeMessage = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":                          # find the end of the length
                j += 1

            length = int(s[i:j])                        # digits before the "#"
            start = j + 1                               # first character of the word
            decodeMessage.append(s[start : start + length])     # take exactly `length` characters

            i = start + length                          # jump to the next length

        return decodeMessage