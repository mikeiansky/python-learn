

def add(x):
    yield x + 1
    yield x + 2
    yield x + 3
    print('complete')
    return x + 6


ga = add(4)


for v in ga:
    print(v)