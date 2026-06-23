def maxOperations(nums, k):
    nums.sort()
    left = 0
    right = len(nums)-1
    count = 0
    while left < right:
        sum = nums[left] + nums[right]
        if sum == k:
            count = count + 1
            left = left + 1
            right = right - 1
        elif sum < k:
            left = left + 1
        else:
            right = right - 1
    return count

count = maxOperations([1,2,3,4], 5)
print(count)