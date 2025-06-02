#keyEvent

import tkinter

#전역변수
key = 0
cx = 400
cy = 300

#함수
def main_proc():
    global cx, cy
    #lable["text"] = key
    
    # 키보드 입력을 통해 이미지의 위치 변경
    if key == "Up":
        cy -= cy - 20
    if key == "Down":
        cy += cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20

    #시간에 따라 캐릭터가 내려가
    cy += 10

    #변경된 위치에 경계를 확인 >> 이미지가 창을 벗어나지 않도록
    if cy < 50 : cy = 50
    if cy > 550 : cy = 550
    if cx < 50 : cx = 50
    if cx > 750 : cx = 750
    
    #변경된 위치에 이미지를 옮김
    canvas.coords("chii",cx,cy)
    root.after(100,main_proc)

def key_down(e):
    global key  #>>전역변수임을알리기위해?사용
    key = e.keysym #keycode를 ketsym으로 바꿔적음 keycode는 숫자가 뜨는데 요거는 입력한 그대로 나옴

def key_up(e):
    global key
    key = 0

#메인
root = tkinter.Tk()
root.title("키이벤트")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
#lable = tkinter.Label(font=("맑은 고딕",80))
#lable.pack()
canvas  = tkinter.Canvas(width=800,height=600,bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="chii.png")
canvas.create_image(400,300, image=img,tag="chii")
canvas.coords("chii",500,400)

main_proc()
root.mainloop()