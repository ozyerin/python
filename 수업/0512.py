#read.py로 파일 이름 설정하심....
#왜 텍스트 파일을 못읽을까..^^!~~~

'''
file = open("test.txt","r",encoding="UTF-8")

for i in range(0,19,1):
    str = file.readline()
    print(str,end='')'


while True:
    str = file.readline()
    print(str,end='')
    if(str == ""):
        break

file.close()


file = open("test.txt","r",encoding="UTF-8")

fileList = file.readlines()
for str in fileList :
    print(str,end="")

file.close()

file = open("test.txt","r",encoding="UTF-8")

fileList = file.readlines()
index = 1
for str1 in fileList :
    print(str(index)+":"+str1,end="")
    index = index + 1

file.close()

'''

import tkinter

root = tkinter.Tk()

file = open("test.txt","r",encoding="UTF-8")

strFile = file.readline()
root.title(strFile[:-1])

strFile = file.readline()
root.geometry(strFile[:-1])

file.close()

root.mainloop()