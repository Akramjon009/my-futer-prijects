class Solution:
    def addTwoNumbers(self, l1):
        l1 = map(str, l1)
        return list(map(int, str(int("".join(l1)) + 1)))


print(Solution().addTwoNumbers([2, 4, 3]))