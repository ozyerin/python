'''

def sumFunc(user):
    print(user+"님. 두 숫자를 입력하세요.")
    num1 = int(input("정수1==>"))
    num2 = int(input("정수2==>"))
    hap = num1 + num2
    return hap

hap = sumFunc("A")
print("결과 : ", hap)
hap = sumFunc("B")
print("결과 : ", hap)
hap = sumFunc("C")
print("결과 : ", hap)


def clac(v1,v2,op):
    if (op == "+" ):
        result = v1 + v2
    elif (op == "*"):
        result = v1 * v2
    elif (op == "/"):
        result = v1 / v2
    elif (op == "-"):
        result = v1 - v2 
    return result


op = input("계산 입력:")
v1 = int(input("첫 번째 숫자 입력 : "))
v2 = int(input("첫 번째 숫자 입력 : "))
value = clac(v1,v2,op)
print(result)




ㅎ.. 졸아서 뭐하는건지 모르겠음
'''

import tkinter

tmr = 0

#함수선언
def countUp():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(100,countUp)

#메인함수
root = tkinter.Tk()
root.title("개졸려")
root.geometry("300x200")

label = tkinter.Label(text=0,font=("궁서체",80))
label.pack()

root.after(100,countUp)

root.mainloop
