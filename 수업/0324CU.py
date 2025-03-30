import tkinter
import tkinter.font

def btn_click():
     num1 = int(entry1.get())
     num2 = int(entry2.get())
     num3 = int(entry3.get())
     num4 = int(entry4.get())
     num5 = int(entry5.get())
     num6 = int(entry6.get())
     num7 = int(entry7.get())
     num8 = int(entry8.get())
     num9 = int(entry9.get())
     num10 = int(entry10.get())
     num11 = int(entry11.get())
     num12 = int(entry12.get())

     str1 = str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
     labelRes1 = tkinter.Label(root,text=str1,font=("맑은고딕", 10))
     labelRes1.place(x=20,y=90)



root = tkinter.Tk()
root.title("CU")
root.geometry("800x300")

label1 = tkinter.Label(root, text="캔 커피",font=("맑은고딕", 10))
label2 = tkinter.Label(root, text="삼각김밥",font=("맑은고딕", 10))
label3 = tkinter.Label(root, text="바나나 우유",font=("맑은고딕", 10))
label4 = tkinter.Label(root, text="도시락",font=("맑은고딕", 10))
label5 = tkinter.Label(root, text="콜라",font=("맑은고딕", 10))
label6 = tkinter.Label(root, text="새우깡",font=("맑은고딕", 10))
label7 = tkinter.Label(root, text="판매 수량", font=("맑은고딕",10))
label8 = tkinter.Label(root, text="구매 수량", font=("맑은고딕",10))
label1.place(x=110,y=30)
label2.place(x=225,y=30)
label3.place(x=340,y=30)
label4.place(x=470,y=30)
label5.place(x=595,y=30)
label6.place(x=710,y=30)
label7.place(x=15,y=80)
label8.place(x=15,y=130)

entry1 = tkinter.Entry(width=8)
entry2 = tkinter.Entry(width=8)
entry3 = tkinter.Entry(width=8)
entry4 = tkinter.Entry(width=8)
entry5 = tkinter.Entry(width=8)
entry6 = tkinter.Entry(width=8)
entry7 = tkinter.Entry(width=8)
entry8 = tkinter.Entry(width=8)
entry9 = tkinter.Entry(width=8)
entry10 = tkinter.Entry(width=8)
entry11 = tkinter.Entry(width=8)
entry12 = tkinter.Entry(width=8)
entry1.place(x=105,y=80)
entry2.place(x=225,y=80)
entry3.place(x=345,y=80)
entry4.place(x=465,y=80)
entry5.place(x=585,y=80)
entry6.place(x=705,y=80)
entry7.place(x=105,y=130)
entry8.place(x=225,y=130)
entry9.place(x=345,y=130)
entry10.place(x=465,y=130)
entry11.place(x=585,y=130)
entry12.place(x=705,y=130)

btn = tkinter.Button(root, text="계산",font=("맑은고딕", 10))
btn.place(x=100,y=180,width=670,height=30)




root.mainloop()