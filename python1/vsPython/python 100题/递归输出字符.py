def out(s,l):
    if l == 0:
        return
    print(s[l-1])
    out(s,l-1)

s = input()
l = len(s)
out(s,l)