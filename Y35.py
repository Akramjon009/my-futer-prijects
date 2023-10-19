class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets = [i for i in s if i.isalpha()][-1::-1]
        for i in range(len(s)):
            if not(s[i].isalpha()):
                alphabets.insert(i, s[i])
        alphabets = ''.join(alphabets)
        return alphabets