N, X = map(int, input().split(' '))
S = input()

for s in S:
    if s == 'U':
        X = X >> 1
    if s == 'L':
        X = X << 1
    if s == 'R':
        X = (X << 1) + 1

print(X)