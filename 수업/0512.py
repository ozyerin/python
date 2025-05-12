#read.py로 파일 이름 설정하심....
#왜 텍스트 파일을 못읽을까..^^!~~~


#파일 읽는거

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

import tkinter

root = tkinter.Tk()

file = open("C:/Users/user/Desktop/python/수업/test.txt","r",encoding="UTF-8")

strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])

file.close()

root.mainloop()


#파일 이름 write.py로 하심용 이번엔 쓰기 입니더...

outFile = open("C:/Users/user/Desktop/python/수업/outTest.txt","w",encoding="UTF-8")

while True :
    outStr = input("내용입력==>")
    #사용자가 끝이라 입력하면 종료
    if outStr == '끝':
        break
    outFile.writelines(outStr+"\n")


outFile.close()

'''

#copyCopy.py == > test파일을 읽어와서 outtest파일에 적용


inFile = open("C:/Users/user/Desktop/python/수업/test.txt","r",encoding="UTF-8")
outFile = open("C:/Users/user/Desktop/python/수업/outTest.txt","w",encoding="UTF-8")

while True:
    strFile = inFile.readline()
    if(str==""):
        break
    outFile.writelines(strFile)

inFile.close()
outFile.close()