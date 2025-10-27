
s = input().strip()

#print(s)
a = s.split()
s = ''.join(a)

stack = [1]
sign = 1

res = 0
chislo = 0

for i in range(len(s)):
    if s[i] == "-":
        res += sign * chislo
        chislo = 0
        sign = -stack[-1]
    elif s[i] == "+":
        res += sign * chislo
        chislo = 0
        sign = stack[-1]
    elif s[i] == "(":
        res += sign * chislo
        chislo = 0
        stack.append(sign)
    elif s[i] == ")":
        res += sign * chislo
        chislo = 0
        stack.pop()
    else:
        chislo = chislo*10+int(s[i])

res+=sign * chislo

print(res)
