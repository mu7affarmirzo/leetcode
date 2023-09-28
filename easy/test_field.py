def infinite_generator():
    i = 0
    while True:
        yield i
        i += 1


for i in range(19):
    a = infinite_generator()
