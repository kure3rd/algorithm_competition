from collections import defaultdict

N = int(input())
X = list()
for n in range(N):
    X.append(tuple(map(int, input().split(' '))))
S = input()

Y = defaultdict(lambda: defaultdict(dict))
for (x, y), lr in zip(X, S):
    if lr == 'L':
        if isinstance(Y[y][lr], dict):
            Y[y][lr] = 0
        Y[y][lr] = max(Y[y][lr], x)
    if lr == 'R':
        if isinstance(Y[y][lr], dict):
            Y[y][lr] = float('inf')
        Y[y][lr] = min(Y[y][lr], x)

for XS in Y.values():
    #print(XS)
    if isinstance(XS['R'], dict) or isinstance(XS['L'], dict):
        continue
    if XS['R'] < XS['L']:
        print('Yes')
        break
else:
    print('No')