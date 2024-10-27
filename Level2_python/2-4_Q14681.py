# 한 번에 사분면 입력X, 한 줄 씩 따로 x, y 좌표 각각 입력하기
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")