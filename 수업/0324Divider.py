import tkinter

# 버튼 클릭하면 실행댐
def btn_click():
    # 값 입력 (글자여서 숫자로 바꿔야댐)
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    # 라벨에 넣을 문자열 
    str1 = str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    # 라벨 만들거
    labelRes1 = tkinter.Label(root,text=str1,font=("맑은고딕", 10))
    labelRes1.place(x=20,y=90)

    str2 = str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지는 "+str(num1%num2)+"입니다."
    labelRes2 = tkinter.Label(root,text=str2,font=("맑은고딕", 10))
    labelRes2.place(x=20,y=110)

def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+","+str(y))
    labelMouse.place(x=1,y=250)
    '''
    이걸 요기에다 걍 갖다 붙이면
    labelMouse = tkinter.Label(root,text=str(x)+","+str(y),font=("맑은고딕", 10))
    labelMouse.place(x=1,y=250)
    마우스를 움직이는 만큼 라벨은 만들어 붙이는 거라 보면 됨 메모리 많이 잡아먹는다 ㅋㅋ
    '''

    
root = tkinter.Tk()
root.title("계산을 합시더")
root.geometry("400x300")
# 좌표 출력기 (루트 지오매트리 이거 밑에 쓰면 댐)
root.bind("<Motion>",mouseMove)
labelMouse = tkinter.Label(root,text=",",font=("맑은고딕", 10))
# 그래서 라벨 이거를 여기에 붙어야 댐..


label1 = tkinter.Label(root, text="나눠 지는 수",font=("맑은고딕", 10))
label2 = tkinter.Label(root, text="나누는 수",font=("맑은고딕", 10))
label1.place(x=20,y=20)
label2.place(x=20,y=45)

entry1 = tkinter.Entry(width=8)
entry2 = tkinter.Entry(width=8)
entry1.place(x=110,y=20)
entry2.place(x=110,y=45)

btn = tkinter.Button(root, text="계산",font=("맑은고딕", 10),command=btn_click)
btn.place(x=200,y=20,width=50,height=45)

root.mainloop()

# 샵하고 작성하면 주석이 생긴답니다.. 나중에 수업 들으면서 적으면서 하지 말고 걍 이걸로 쓰면서 수업 내용 필기하면 ㄱㅊ을거 같음
'''
오잉 이렇게 해도 주석이 생긴다 함 여러 문장 쓸 때
쓰면 되느거라 함니다 와웅
'''

