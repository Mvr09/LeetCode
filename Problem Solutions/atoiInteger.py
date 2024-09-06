class Solution:
    def myAtoi(self, s: str) -> int:
        def validate(x):
            if x>(2**32)-1:
                return (2**31)-1
            elif x<(-2**31):
                return (-2**31)
            else:
                return x
        s = s.lstrip()
        s = s.strip('"')

        negative = False
        if s[0] == "-":
            negative = True
            s = s[1::1]
        elif s[0] == "+":
            negative = False
            s = s[1::1]
        elif s[0] not in "1234567890.-+":
            return 0
        for i in range(len(s)):
            if s[i] not in "1234567890.-+":
                s = s[:i:]
                break
        if negative:
            return validate(int(s) * -1)
        try:
            return validate(int(s))
        except:
            return 0


def myAtoi(s: str) -> int:
    s = s.lstrip()
    negative = False
    if s[0] == "-":
        negative = True
        s = s[1::1]
    elif s[0] == "+":
        negative = False
        s = s[1::1]
    elif s[0] not in "1234567890.-+":
        return 0
    for i in range(len(s)):
        if s[i] not in "1234567890.-+":
            s = s[:i:]
            break
    if negative:
        return int(s) * -1
    return int(s)

print(myAtoi("words and 987"))