n = 10203004

sum = 0
x = 0
while (n>0):
    digit  = n % 10
    if digit != 0:
        sum = sum + digit
        x = x * 10 + digit
    n = n //10
    rev = int(str(x)[::-1])

print(rev*sum)