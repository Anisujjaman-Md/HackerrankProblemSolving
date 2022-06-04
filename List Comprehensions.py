import itertools
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
def loop():
    s = [[i, j, k] for i, j, k in itertools.product(range(x + 1), range(y + 1), range(z + 1)) if i + j + k != n]
    print(s)
loop()