#keyEvent

import tkinter

#전역변수
key = 0

#함수
def main_proc():
    #lable["text"] = key
    root.after(100,main_proc)

def key_down(e):
    global key  #>>전역변수임을알리기위해?사용
    key = e.keysym #keycode를 ketsym으로 바꿔적음 keycode는 숫자가 뜨는데 요거는 입력한 그대로 나옴

#메인
root = tkinter.Tk()
root.title("키이벤트")
root.bind("<KeyPress>",key_down)
#lable = tkinter.Label(font=("맑은 고딕",80))
#lable.pack()
canvas  = tkinter.Canvas(width=800,height=600,bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="chi.png")
canvas.create_image(400,300, Image=img)

main_proc()
root.mainloop()