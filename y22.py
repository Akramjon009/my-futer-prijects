class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = map(str, l1)
        l2 = map(str, l2)
        return list(map(int, (str(int("".join(l1)) + int("".join(l2))))[::-1]))


print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))