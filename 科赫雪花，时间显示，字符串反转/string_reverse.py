def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[0:-1])


l = 'abcdefg'
s2 = reverse(l)
print(s2)


