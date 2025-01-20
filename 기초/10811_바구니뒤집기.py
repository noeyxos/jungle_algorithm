# 바구니 뒤집기
# https://www.acmicpc.net/problem/10811

nums = [1, 2, 3, 4, 5]

print(nums[1])
print(nums[1:4])
nums[4] = nums[2]
nums[2] = nums[4]
print(nums)