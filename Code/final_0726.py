#-*- coding: utf-8 -*-
import os
import sys
##import urllib.request
import serial
import pygame  
 
port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

aa = []
i = 0
hap = str()
a = 0 ## 초성
b = 0 ## 중성
c = 0 ## 종성
tmp = 0 ## shift 눌름 상태 확인 변수
mid = 0 ## 이중 모음 구분 변수
inputc = 0
data = str()

while True:
    input_s = serialFromArduino.readline()
    inputa = int(input_s)
    if(tmp == 2):  ## shift누르고 이중모음 앞 6점 눌렀을 때
        if(mid == 0 and inputa == 1235):  ## ㅒ
            b = 3
            mid = 0
            tmp = 0
        elif(mid == 1 and inputa == 1235):  ## ㅙ
            b = 10
            mid = 0
            tmp = 0
        elif(mid == 2 and inputa == 1235):  ## ㅞ
            b = 15
            mid = 0
            tmp = 0
        elif(mid == 3 and inputa == 1235):  ##ㅟ
            b = 16
            mid = 0
            tmp = 0
    elif(tmp == 1):  ## shift 눌렀을 때
        if(inputa == 4):  ## 초성 시작
            a = 1
            tmp = 0
        elif(inputa == 9):
            aa.append(" ");
            tmp = 0
        elif(inputa == 14):
            a = 2
            tmp = 0
        elif(inputa == 24):
            a = 4
            tmp = 0
        elif(inputa == 5):
            a = 5
            tmp = 0
        elif(inputa == 15):
            a = 6
            tmp = 0
        elif(inputa == 45):
            a = 8
            tmp = 0
        elif(inputa == 10):  ##shift
            tmp = 1
        elif(inputa == 1245):
            a = 11
            tmp = 0
        elif(inputa == 46):
            a = 13
            tmp = 0
        elif(inputa == 56):
            a = 14
            tmp = 0
        elif(inputa == 124):
            a = 15
            tmp = 0
        elif(inputa == 125):
            a = 16
            tmp = 0
        elif(inputa == 145):
            a = 17
            tmp = 0
        elif(inputa == 245):
            a = 18
            tmp = 0

        if(inputa == 126):  ## 중성 시작
            tmp = 2
            mid = 1
        elif(inputa == 1235):
            b = 1
        elif(inputa == 345):
            tmp = 2
            mid = 0
        elif(inputa == 234):
            b = 4
        elif(inputa == 1345):
            b = 5
        elif(inputa == 156):
            b = 6
        elif(inputa == 34):
            b = 7
        elif(inputa == 136):
            b = 8
        elif(inputa == 1236):
            b = 9
        elif(inputa == 13456):
            b = 11
        elif(inputa == 346):
            b = 12
        elif(inputa == 134):
            tmp = 2
            mid = 3
        elif(inputa == 1234):
            tmp = 2
            mid = 2
        elif(inputa == 146):
            b = 17
        elif(inputa == 246):
            b = 18
        elif(inputa == 2456):
            b = 19
        elif(inputa == 135):
            b = 20

        if (inputc == 1 and inputa == 1):
            c = 2
        elif (inputc == 1 and inputa == 3):
            c = 3
        elif (inputc == 2 and inputa == 1):
            c = 9
        elif (inputa == 1):  ##종성 시작
            inputc = 1
            c = 1
        elif (inputc == 25 and inputa == 13):
            c = 5
        elif (inputc == 25 and inputa == 356):
            c = 6
        elif (inputa == 25):
            inputc = 25
            c = 4
        elif (inputa == 35):
            c = 7
        elif (inputc == 2 and inputa == 26):
            c = 10
        elif (inputa == 26):
            c = 16
        elif (inputc == 2 and inputa == 12):
            c = 11
        elif (inputa == 12):
            inputc = 12
            c = 17
        elif (inputc == 2 and inputa == 3):
            c = 12
        elif (inputa == 3):
            c = 19
        elif (inputc == 2 and inputa == 236):
            c = 13
        elif (inputa == 236):
            c = 25
        elif (inputc == 2 and inputa == 256):
            c = 14
        elif (inputa == 256):
            c = 26
        elif (inputc == 2 and inputa == 356):
            c = 15
        elif (inputa == 356):
            c = 27
        elif (inputa == 2):
            inputc = 2
            c = 8
        elif (inputc == 12 and inputa == 3):
            c = 18
        elif (inputa == 34):  ##약어 ㅆ
            c = 20
        elif (inputa == 2356):
            c = 21
        elif (inputa == 13):
            c = 22
        elif (inputa == 23):
            c = 23
        elif (inputa == 235):
            c = 24

        '''if(inputa == 3456):
            bb[3] = 1

        if(bb[3] == 1 and inputa == 1):
            aa.append("1")
        elif(bb[3] == 1 and inputa == 12):
            aa.append("2")

        if(bb[3] == 1 and inputa == 14):
            aa.append("3")
        elif(bb[3] == 1 and inputa == 145):
            aa.append("4")
        elif(bb[3] == 1 and inputa == 15):
            aa.append("5")
        elif(bb[3] == 1 and inputa == 124):
            aa.append("6")
        elif(bb[3] == 1 and inputa == 1245):
            aa.append("7")
        elif(bb[3] == 1 and inputa == 125):
            aa.append("8")
        elif(bb[3] == 1 and inputa == 24):
            aa.append("9")
        elif(bb[3] == 1 and inputa == 245):
            aa.append("0")
        elif(bb[3] == 1 and inputa == 3456):
            bb[3] = 0

        if(inputa == 356):
            bb[4] = 1

        if(bb[4] == 1 and inputa == 1):
            aa.append("a")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 12):
            aa.append("b")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 14):
            aa.append("c")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 145):
            aa.append("d")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 15):
            aa.append("e")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 124):
            aa.append("f")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1245):
            aa.append("g")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 125):
            aa.append("h")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 24):
            aa.append("i")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 245):
            aa.append("j")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 13):
            aa.append("k")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 123):
            aa.append("l")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 134):
            aa.append("m")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1345):
            aa.append("n")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 135):
            aa.append("o")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1234):
            aa.append("p")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 12345):
            aa.append("q")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1235):
            aa.append("r")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 234):
            aa.append("s")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 2345):
            aa.append("t")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 136):
            aa.append("u")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1236):
            aa.append("v")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 2456):
            aa.append("w")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1346):
            aa.append("x")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 13456):
            aa.append("y")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 1356):
            aa.append("z")
            del aa[len(aa)-4:len(aa)-1]
        elif(bb[4] == 1 and inputa == 256):
            bb[4] = 0'''

        hangul = chr(588 * a + 28 * b + c + 0xAC00)  ##유니코드를 한글로 조합
        if (inputa == 7):  ## 한글로 합치기
            aa.append(hangul)
            a = 0  ##초성 초기화
            b = 0  ##중성 초기화
            c = 0  ##종성 초기화

        if (inputa == 8):  ## enter
            for i in range(0, len(aa), 1):
                hap += aa[i]

                if (len(hap) == len(aa)):
                    print(hap)  ##한글 출력
                    del aa[0:len(aa)]
                    hap = str()

        if(inputa == 10):  ## back spacebar
            del aa[len(aa)-1:len(aa)]
    elif(tmp == 0):
            if(inputa == 4):   ##초성 시작
                a = 0
            elif(inputa == 9):  ##spacebar
                aa.append(" ");
            elif(inputa == 14):
                a = 2
            elif(inputa == 24):
                a = 3
            elif(inputa == 5):
                a = 5
            elif(inputa == 15):
                a = 6
            elif(inputa == 45):
                a = 7
            elif(inputa == 10):  ##shift
                tmp = 1
            elif(inputa == 1245):
                a = 11
            elif(inputa == 46):
                a = 12
            elif(inputa == 56):
                a = 14
            elif(inputa == 124):
                a = 15
            elif(inputa == 125):
                a = 16
            elif(inputa == 145):
                a = 17
            elif(inputa == 245):
                a = 18

            if(inputa == 126):  ##중성 시작
                b = 0
            elif(inputa == 1235):
                b = 1
            elif(inputa == 345):
                b = 2
            elif(inputa == 234):
                b = 4
            elif(inputa == 1345):
                b = 5
            elif(inputa == 156):
                b = 6
            elif(inputa == 34):
                b = 7
            elif(inputa == 136):
                b = 8
            elif(inputa == 1236):
                b = 9
            elif(inputa == 13456):
                b = 11
            elif(inputa == 346):
                b = 12
            elif(inputa == 134):
                b = 13
            elif(inputa == 1234):
                b = 14
            elif(inputa == 146):
                b = 17
            elif(inputa == 246):
                b = 18
            elif (inputa == 2456):
                b = 19
            elif(inputa == 135):
                b = 20

            if (inputc == 1 and inputa == 1):
                c = 2
            elif (inputc == 1 and inputa == 3):
                c = 3
            elif (inputc == 2 and inputa == 1):
                c = 9
            elif (inputa == 1):  ##종성 시작
                inputc = 1
                c = 1
            elif (inputc == 25 and inputa == 13):
                c = 5
            elif (inputc == 25 and inputa == 356):
                c = 6
            elif (inputa == 25):
                inputc = 25
                c = 4
            elif (inputa == 35):
                c = 7
            elif (inputc == 2 and inputa == 26):
                c = 10
            elif (inputa == 26):
                c = 16
            elif (inputc == 2 and inputa == 12):
                c = 11
            elif (inputa == 12):
                inputc = 12
                c = 17
            elif (inputc == 2 and inputa == 3):
                c = 12
            elif (inputc == 12 and inputa == 3):
                c = 18
            elif (inputa == 3):
                c = 19
            elif (inputc == 2 and inputa == 236):
                c = 13
            elif (inputa == 236):
                c = 25
            elif (inputc == 2 and inputa == 256):
                c = 14
            elif (inputa == 256):
                c = 26
            elif (inputc == 2 and inputa == 356):
                c = 15
            elif (inputa == 356):
                c = 27
            elif (inputa == 2):
                inputc = 2
                c = 8
           
            elif (inputa == 34):  ##약어 ㅆ
                c = 20
            elif (inputa == 2356):
                c = 21
            elif (inputa == 13):
                c = 22
            elif (inputa == 23):
                c = 23
            elif (inputa == 235):
                c = 24

            '''if(inputa == 3456):
                bb[3] = 1

            if(bb[3] == 1 and inputa == 1):
                aa.append("1")
            elif(bb[3] == 1 and inputa == 12):
                aa.append("2")

            if(bb[3] == 1 and inputa == 14):
                aa.append("3")
            elif(bb[3] == 1 and inputa == 145):
                aa.append("4")
            elif(bb[3] == 1 and inputa == 15):
                aa.append("5")
            elif(bb[3] == 1 and inputa == 124):
                aa.append("6")
            elif(bb[3] == 1 and inputa == 1245):
                aa.append("7")
            elif(bb[3] == 1 and inputa == 125):
                aa.append("8")
            elif(bb[3] == 1 and inputa == 24):
                aa.append("9")
            elif(bb[3] == 1 and inputa == 245):
                aa.append("0")
            elif(bb[3] == 1 and inputa == 3456):
                bb[3] = 0

            if(inputa == 356):
                bb[4] = 1

            if(bb[4] == 1 and inputa == 1):
                aa.append("a")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 12):
                aa.append("b")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 14):
                aa.append("c")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 145):
                aa.append("d")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 15):
                aa.append("e")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 124):
                aa.append("f")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1245):
                aa.append("g")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 125):
                aa.append("h")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 24):
                aa.append("i")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 245):
                aa.append("j")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 13):
                aa.append("k")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 123):
                aa.append("l")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 134):
                aa.append("m")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1345):
                aa.append("n")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 135):
                aa.append("o")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1234):
                aa.append("p")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 12345):
                aa.append("q")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1235):
                aa.append("r")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 234):
                aa.append("s")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 2345):
                aa.append("t")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 136):
                aa.append("u")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1236):
                aa.append("v")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 2456):
                aa.append("w")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1346):
                aa.append("x")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 13456):
                aa.append("y")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 1356):
                aa.append("z")
                del aa[len(aa)-4:len(aa)-1]
            elif(bb[4] == 1 and inputa == 256):
                bb[4] = 0'''

            hangul = chr(588 * a + 28 * b + c + 0xAC00)  ##유니코드를 한글로 조합
            if (inputa == 7):  ## 한글로 합치기
                aa.append(hangul)
                a = 0  ##초성 초기화
                b = 0  ##중성 초기화
                c = 0  ##종성 초기화
                inputc = 0

            if (inputa == 8):  ## enter
                for i in range(0, len(aa), 1):
                    hap += aa[i]

                    if (len(hap) == len(aa)):
                        print(hap)  ##한글 출력
                        del aa[0:len(aa)]
                        hap = str()

            if(inputa == 10):  ## back spacebar
                del aa[len(aa)-1:len(aa)]