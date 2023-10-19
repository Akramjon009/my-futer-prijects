class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        nums = int()
        for i in range(len(s)):
            if s[i].isdecimal():
                if int(s[i]) > nums:
                    nums = int(s[i])
                else:
                    return False
        return True

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
new = Solution()
print(new.areNumbersAscending(s))