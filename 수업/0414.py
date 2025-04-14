#실습2 구구단 코드 만들자 ㅈㄴ 개큰 지각 함

for num1 in range(2,10,1): #단
    for num2 in range(1,10,1): #곱해지는 수
       # print("----구구단", num1,"단-----")
        print(num1,"X",num2,"=\t",num1*num2) #\t하면 줄 정렬 정돈 됨
        pass

#while
#i = 0
#while(i < 3):
#    print("ㅎ", end="")


#무한루프 되는 거 터미널 부분에다 ctrl+c 하면 멈춤
'''
while(True):
    num1 = int(input("숫자1===> "))
    #num1이 0이면 반복문 종료
    if num1 == 0:
        break
    num2 = int(input("숫자2===> "))
    res = num1 + num2
    print(num1,"+",num2,"=",num1 + num2)

'''

#연습
#1부터 100까지 더하되 4의 배수는 더하지 않음
#3의 배수도 더하지 않음

res = 0
for i in range(1,101,1):
    if 1 % 4 == 0:
        continue
    elif 1 % 3 == 0:
        continue
    res = res + i
    print(res)

    #2499가 나와야 하는데 왜.,... 난,,,,,,,