import tkinter
import tkinter.font

def click_btn():
    labelE = tkinter.Label(root, text="동",font=("궁서",24))
    labelW = tkinter.Label(root, text="서",font=("궁서",24))
    labelS = tkinter.Label(root, text="남",font=("궁서",24))
    labelN = tkinter.Label(root, text="북",font=("궁서",24))
    labelE.place(x=500,y=300)
    labelW.place(x=300,y=300)
    labelS.place(x=400,y=400)
    labelN.place(x=400,y=200)

    txt = entry.get()
    str1 = txt
    labeltxt = tkinter.Label(root, text=str1,font=("궁서",10))
    labeltxt.place(x=450,y=350)


root = tkinter.Tk()

root.title("첫 번째 윈도우")
root.geometry("800x600")

btn = tkinter.Button(root,text="버튼",font=("궁서",10),command=click_btn)
btn.place(x=400,y=300,width=40,height=30)

entry = tkinter.Entry(width=5)
entry.place(x=400,y=350)

root.mainloop()
