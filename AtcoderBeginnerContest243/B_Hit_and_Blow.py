N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

eq = 0
for a, b in zip(A, B):
    if a == b:
        eq += 1

neq = len(set(A) & set(B)) - eq

print(eq)
print(neq)