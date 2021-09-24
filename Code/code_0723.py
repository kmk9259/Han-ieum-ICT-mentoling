#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import serial
import pygame

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()
cho_arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
jung_arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
jong_arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
aa = []
bb = [0,0,0,0,0,0,0]
i = 0
hap = str()
a = 0
b = 0
c = 0
data = str()

while True:
    input_s = serialFromArduino.readline()
    inputa = int(input_s)
    if(inputa == 4):
        a = 0
    
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
    elif(inputa == 6):
        a = 9
        bb[0] = 1
        bb[2] = 4
        if(bb[0] == 1 and inputa == 4):
            a = 1
        elif(bb[0] == 1 and inputa == 24):
            a = 4
        elif(bb[0] == 1 and inputa == 45):
            a = 8
        elif(bb[0] == 1 and inputa == 6):
            a = 10
        elif(bb[0] == 1 and inputa == 46):
            a = 13
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
           
    if(inputa == 126):
        b = 0
    elif(bb[1] == 0 and inputa == 1235):
        b = 1
    elif(inputa == 345):
        b = 2
        bb[1] = 1
    if(bb[1] == 1 and inputa == 1235):
        b = 3
        bb[1] = 0
    elif(inputa == 234):
        b = 4
    elif(bb[1] == 0 and inputa == 1345):
        b = 5
    elif(inputa == 156):
        b = 6
    elif(inputa == 34):
        b = 7
    elif(inputa == 136):
        b = 8
    elif(inputa == 1236):
        b = 9
        bb[1] = 2
    if(bb[1] == 2 and inputa == 1235):
        b = 10
        bb[1] = 0
    elif(inputa == 13456):
        b = 11
    elif(inputa == 346):
        b = 12
    elif(inputa == 134):
        b = 13
        bb[1] = 4
    if(bb[1] == 4 and inputa == 1235):
        b = 16
        bb[1] = 0
    elif(inputa == 1234):
        b = 14
        bb[1] = 3
    if(bb[1] == 3 and inputa == 1235):
        b = 15
        bb[1] = 0
    elif(inputa == 146):
        b = 17
    elif(inputa == 246):
        b = 18
    elif(inputa == 135):
        b = 20
    elif(inputa == 2456):
        b = 19
    
    if(inputa == 1):
        c = 1
        bb[2] = 4
        if(bb[2] == 4 and inputa == 1):
            c = 2
        elif(bb[2] == 4 and inputa == 3):
            c = 3
    elif(inputa == 25):
        c = 4
        bb[2] = 4
        if(bb[2] == 4 and inputa == 13):
            c = 5
        elif(bb[2] == 4 and inputa == 356):
            c = 6
    elif(inputa == 35):
        c = 7
    elif(inputa == 2):
        c = 8
        bb[2] = 4
        if(bb[2] == 4 and inputa == 1):
            c = 9
        elif(bb[2] == 4 and inputa == 12):
            c = 10
        elif(bb[2] == 4 and inputa == 3):
            c = 11
        elif(bb[2] == 4 and inputa == 236):
            c = 12
        elif(bb[2] == 4 and inputa == 256):
            c = 13
        elif(bb[2] == 4 and inputa == 356):
            c = 14
    elif(inputa == 26):
        c = 15
    elif(inputa == 12):
        c = 16
        bb[2] = 4
        if(bb[2] == 4 and inputa == 3):
            c = 17
        elif(bb[2] == 4 and inputa == 12):
            c = 18
    elif(inputa == 3):
        c = 19
    elif(inputa == 34):
        c = 20
    elif(inputa == 2356):
        c = 21
    elif(inputa == 13):
        c = 22
    elif(inputa == 23):
        c = 23
    elif(inputa == 235):
        c = 24
    elif(inputa ==236):
        c = 25
    elif(inputa == 256):
        c = 26
    elif(inputa == 356):
        c = 27
    
    if(inputa == 3456):
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
            bb[4] = 0
    
    hangul = chr(588*a + 28*b + c +0xAC00)
    if(inputa == 8):## spacebar
            aa.append(hangul)
            a = 0
            b = 0
            c = 0
        
    if(inputa == 9): ## enter
        for i in range(0,len(aa),1):
            hap += aa[i]
            if(len(hap) == len(aa)):
                print(hap)
                del aa[0:len(aa)]
                
                hap = str()
                
    ##if(inputa == 9): ## backspacebar
     ##   del aa[len(aa)-1:len(aa)]
      ##  bb[6] = 1
       ##print(bb)
    
    elif(inputa == 10): ## sound
        file = 'sound.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        bb[5] = 1
        bb[6] = 0
        print(bb)
            
    elif(inputa == 11): ## sound1
        file = 'sound1.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        bb[5] = 2
        
    while (bb[5] == 1 and bb[6] == 0 and inputa == 8):
        data = input()
        client_id = "AdtDtGbL3cCi8pel3VrJ"
        client_secret = "_AgNot0Up_"
        encText = urllib.parse.quote(data)
        data = "speaker=jinho&speed=0&text=" + encText;
        url = "https://openapi.naver.com/v1/voice/tts.bin"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            with open('sound1.mp3', 'wb') as f:
                f.write(response_body)
            bb[5] = 0
        else:
            print("Error Code:" + rescode)
        if(bb[5] == 2):
            break
        