A, B = input().split()
A = int(A) #시작 주파수
B = int(B) #원하는 주파수

n = int(input()) #즐겨찾기된 갯수
N = []
sum = []

temp = A - B
if temp <0 :
    temp = -temp
    
sum.append(temp)

for i in range(n):
    N.append(int(input()))
    temp = N[i] - B
    if temp <0 :
        temp = -temp
    sum.append(temp+1)
print(min(sum))