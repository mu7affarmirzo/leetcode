x = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0, 0]
print(sorted(x))
print(sum(x) - (min(x) + max(x))/20)
l = len(x)
print(x[:l//2+1])
print(x[l//2+1:])
print(''.join([str(i) for i in x]))

[2,3,4] [5,6,7]
