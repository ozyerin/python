import tkinter

def btn_click():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    str1 = str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    labelRes1 = tkinter.Label(root,text=str1,font=("맑은고딕", 10))
    labelRes1.place(x=20,y=90)

    str2 = str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지는 "+str(num1%num2)+"입니다."
    labelRes2 = tkinter.Label(root,text=str2,font=("맑은고딕", 10))
    labelRes2.place(x=20,y=110)


root = tkinter.Tk()
root.title("계산을 합시더")
root.geometry("400x300")

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

