H, M = map(int, input().split())
Timer = int(input())

H += Timer // 60
M += Timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)