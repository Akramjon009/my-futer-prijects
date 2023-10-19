class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        m=''
        while columnNumber:
            columnNumber-=1
            r=columnNumber%26
            columnNumber//=26
            m=chr(65+r)+m
        return m