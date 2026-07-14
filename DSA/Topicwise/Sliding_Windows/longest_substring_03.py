# s = "abcabcbb"

# left = 0
# answer = 0
# window = set()

# for right in range(len(s)):
#     while s[right] in window:
#         window.remove(s[left])
#         left = left +1

#     window.add(s[right])
#     answer = max(answer, right - left + 1)
    
# if answer >0:
#     print(s[left:right+1])

# print(answer)

s = "abcabcbb"

left = 0
answer = 0
start = 0          # Starting index of longest substring
window = set()

for right in range(len(s)):
    while s[right] in window:
        window.remove(s[left])
        left += 1

    window.add(s[right])

    current_length = right - left + 1

    if current_length > answer:
        answer = current_length
        start = left

print("Longest Substring :", s[start:start + answer])
print("Length :", answer)