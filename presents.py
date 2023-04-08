n = int(input())
p = list(map(int, input().split()))

p_inv = [0] * n
for i in range(n):
    p_inv[p[i]-1] = i+1

print(' '.join(map(str, p_inv)))
