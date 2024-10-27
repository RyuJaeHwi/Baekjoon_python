H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
elif H >= 1 and M < 45:
    print(H - 1, (M + 60) - 45)
else:
    # H = 0 인 경우 (자정)
    print(23, (M + 60) - 45)