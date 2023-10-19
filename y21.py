def the_max_minus(nums: list):
    max_minus = nums[0]-nums[1]
    ind = [0, 1]
    for i in range(len(nums)-1):
        if max_minus < nums[i+1]-nums[i]:
            max_minus = nums[i+1]-nums[i]
            ind = [i, i+1]
    return max_minus, ind


nums = input().split()
nums = list(map(int, nums))
minus, ind = the_max_minus(nums)
print(minus, "(", nums[ind[0]], "va", nums[ind[1]], ")")
