s='egg'
t = 'add'

for i in range(len(s)):
    print(t[i], s[i])
    t.replace(str(t[i]), str(s[i]))

print(s, t)
print(t == s)

print(t.replace('d', 'g'))
