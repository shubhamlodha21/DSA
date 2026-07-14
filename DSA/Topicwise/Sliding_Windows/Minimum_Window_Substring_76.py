s = "ADOBECODEBANC"
t = "ABC"
ans = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]

        found = True

        for ch in t:
            if ch not in sub:
                found = False
                break

        if found:
            if ans == "":
                ans = sub
            elif len(sub) < len(ans):
                ans = sub

print(ans)