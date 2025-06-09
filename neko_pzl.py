import tkinter
import random

#전역변수
index = 0
timer = 0
score = 0
hisc = 1000
difficulty = 0
tsugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0


#공간정보 저장
neko = [] #리스트
check = []
for i in range(10): #괄호 8개 공간에 총 10개가 들어?간다고?함 게임공간 가로세로 영역
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])


#블럭정보 저장
blockcount = 

#함수영역
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y #마우스 커서 위치

def mouse_press(e):
    global mouse_c
    mouse_c = 1


def draw_neko():
    cvs.delete("NEKO") # 캔버스에서 태그가 "NEKO"로 되어있는 것을 삭제함
    for y in range(10): # 세로
        for x in range(8): # 가로 >> 이중for문 >> 80개의 모든 칸에서 실행 될 것이다
            if neko[y][x] > 0: # 모든 칸에 대해서 실행
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")
                #x * 72 + 60, y * 72 + 60 >> 이미지에서 게임 영역 네모 칸의 영역과 다음 네모간의 거리, tag="NEKO" >> 태그"NEKO" 생성

def check_neko():
    for y in range(10):
        for x in range(8): #모든 칸에 대해서 실행
            check[y][x] = neko[y][x] # NEKO >> check 복사

    for y in range(1, 9, 1): 
        for x in range(8): #맨위, 맨아래 줄을 제외한 칸에서 실행
            if check[y][x] > 0: #세로 블럭
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7 #관련된 모든 블럭을 7로 변경

    for y in range(10):
        for x in range(1, 7):#맨오른쪽, 맨왼쪽 줄을 제외한 칸에서 실행
            if check[y][x] > 0: #가로블럭
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1, 9):
        for x in range(1, 7): 
            if check[y][x] > 0: #대각선 블럭 
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]: #대각선 유남쌩.. 
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

def sweep_neko(): 
    num = 0
    for y in range(10):
        for x in range(8): #모든 칸에 대해서 실행
            if neko[y][x] == 7:
                neko[y][x] = 0 #빈칸
                num = num + 1 #파괴된 블럭을 표현
    return num

def drop_neko():
    flg = False
    for y in range(8, -1, -1): # 아래에서 위로 검사
        for x in range(8): # 모든 블럭에 대해서 검사
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(8):
        if neko[0][x] > 0: #맨 윗줄에 블럭이 있으면
            return True #게임 종료
    return False

def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(0, difficulty) #블럭을 생성 (0, 1~6: 일반블럭 )

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c
    if index == 0:  # 타이틀 로고
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0
    elif index == 1:  # 타이틀 화면, 시작 대기
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(10):
                for x in range(8):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2:  # 블록 낙하
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓인 블록 확인
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이 블록이 있다면
        sc = sweep_neko()
        score = score + sc * difficulty * 2
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5:  # 마우스 입력 대기
        if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
            cursor_x = int((mouse_x - 24) / 72) # 칸 수만큼 입력 0~7
            cursor_y = int((mouse_y - 24) / 72) # 칸 수만큼 입력 0~9
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)


#메인영역
root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
] #블럭이미지 0,1,2,3,4,5,6,7,8(블럭 터지는 이미지), 기말엔 여기에 조커블럭까지 추가되어져야 함

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()
