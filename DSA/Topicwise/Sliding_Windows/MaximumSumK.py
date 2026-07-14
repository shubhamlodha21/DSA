# Maximum sum of size K

nums = [3,8,2,5,7,6,12]
K = 4
n  = len(nums)

current = 0
for i in range(K):
    current = current + nums[i]
maxx = current

for i in range(1,n-K+1):
    current = current - nums[i-1] + nums[i+K-1]

    if (current > maxx):
        maxx = current

print(maxx) 


