A = int(input())
B = int(input())

B_one = B % 10 # B의 일의 자리 숫자
B_ten = (B // 10) % 10  # B의 십의 자리 숫자
# B = 385일 때, // 을 통해 나눈 수의 정수인 38, 이 수를 10으로 나눈 나머지인 8을 저장
B_hun = B // 100  # B의 백의 자리 숫자

print(A * B_one)
print(A * B_ten)
print(A * B_hun)
print(A * B)