class Solution(object):
    def removeElement(self, nums, val):
        nums2 = list()
        nums3 = list()

        for i in range(len(nums)):
            if nums[i] != val:
                nums2.append(nums[i])
            else:
                nums3.append("_")
        return nums.count(val), nums2+nums3

nums = [0,1,2,2,3,0,4,2]
val = 2
new = Solution().removeElement(nums,val)
print(new)