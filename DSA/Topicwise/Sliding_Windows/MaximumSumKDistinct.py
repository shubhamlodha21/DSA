nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
n = len(nums)

current = 0
for i in range(k):
    current += nums[i]

if len(set(nums[:k])) == k:
    max_sum = current
else:
    max_sum = 0

for i in range(1, n - k + 1):
    current = current - nums[i - 1] + nums[i + k - 1]
    window = nums[i:i + k]
    if len(set(window)) == k:
        max_sum = max(max_sum, current)

print(max_sum)