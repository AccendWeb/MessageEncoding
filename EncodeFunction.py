import sys
import subprocess 
import time 
import os 
import re 
import array 
import base64
from getpass import getpass

#------------ TO-DO -------------

#add total counter on output message
#add positive and negative
#add sections to characters in 3
#make sections within array

#---------------------------------

#declare all base 2 characters
#---------------characters---------------
CharA = 2
CharB = 4 
CharC = 6
CharD = 8
CharE = 10
CharF = 12 
CharG = 14
CharH = 16
CharI = 18
CharJ = 20
CharK = 22
CharL = 24
CharM = 26
CharN = 28
CharO = 30
CharP = 32
CharQ = 34
CharR = 36
CharS = 38
CharT = 40
CharU = 42
CharV = 44
CharW = 46
CharX = 48
CharY = 50
CharZ = 52
#---------------symbols-----------------
Sym1 = 54
Sym2 = 56
Sym3 = 58
Sym4 = 60
Sym5 = 62
Sym6 = 64
Sym7 = 66 
Sym8 = 68
Sym9 = 70
Sym10 = 72
Sym11 = 74
Sym12 = 76
Sym13 = 78
Sym14 = 80
Sym15 = 82
Sym16 = 84
Sym17 = 86
Sym18 = 88
Sym19 = 90
Sym20 = 92
Sym21 = 94
Sym22 = 96 
Sym23 = 98 
Sym24 = 100
Sym25 = 102
Sym26 = 104
Sym27 = 106
Sym28 = 108
Sym29 = 110
Sym30 = 112 
Sym32 = 114
Sym33 = 116
Sym34 = 118
Sym35 = 120
Sym36 = 122
Sym37 = 124
Sym38 = 126
Sym39 = 128
Sym40 = 130
Sym41 = 132
Sym42 = 134
Sym43 = 136
Sym44 = 138
Sym46 = 140
Sym48 = 142
Sym50 = 144
Sym52 = 146
Sym54 = 148
Sym56 = 150
Sym58 = 152
Sym60 = 154
Sym62 = 156
Sym64 = 158
Sym66 = 160
Sym68 = 162
#--------------testing----------------
#InputTestMessge = input("enter test message")
#InputList = list(InputTestMessge)
#InputCount = len(InputTestMessge)
#print(InputTestMessge)
#print(InputList)
#print(InputCount)
#use input for later testing


TestMessage = "wap"

#---------------------------------------

def EncodingBase():
    MessageSplit = list(TestMessage)
    OutputMessage = []
    MessageReOrder = []
    OutputTotal = 0
    InsertString = " \" \" "
    MessageCount = len(MessageSplit)
    for i in range(0, MessageCount):
        MessageReOrder.append(InsertString)

    print(MessageSplit)
    print(MessageCount)
    print(MessageReOrder)

    if 'a' in MessageSplit:
        CountCharA = MessageSplit.count('a')
        Aposition = MessageSplit.index('a')    
        print(Aposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Aposition] #new method

        OutputTotal += 2
        INTposition = MessageReOrder.insert(Aposition, CharA)

        try:
            for CountCharA in range(0, MessageCount):
                Aposition = MessageSplit.index('a')
                OutputTotal += 2
                RMposition =  MessageSplit.remove(Aposition)
                INTposition =  MessageReOrder.insert(Aposition, CharA)
        except:
            print("only one a found")

            print(MessageReOrder)

    
    if 'b' in MessageSplit:
        CountCharB = MessageSplit.count('b')
        Bposition = MessageSplit.index('b')    
        print(Bposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Bposition] #new method

        OutputTotal += 4
        INTposition = MessageReOrder.insert(Bposition, CountCharB)

        try:
            for CountCharA in range(0, MessageCount):
                Bposition = MessageSplit.index('b')
                OutputTotal += 4
                RMposition =  MessageSplit.remove(Bposition)
                INTposition =  MessageReOrder.insert(Bposition, CharB)
        except:
            print("only one b found")

            print(MessageReOrder)

    if 'c' in MessageSplit:
        CountCharC = MessageSplit.count('c')
        Cposition = MessageSplit.index('c')    
        print(Cposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Aposition] #new method

        OutputTotal += 6
        INTposition = MessageReOrder.insert(Cposition, CharC)

        try:
            for CountCharC in range(0, MessageCount):
                Aposition = MessageSplit.index('c')
                OutputTotal += 6
                RMposition =  MessageSplit.remove(Cposition)
                INTposition =  MessageReOrder.insert(Cposition, CharC)
        except:
            print("only one c found")

            print(MessageReOrder)

    if 'd' in MessageSplit:
        CountCharD = MessageSplit.count('d')
        Dposition = MessageSplit.index('d')    
        print(Dposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Dposition] #new method

        OutputTotal += 8
        INTposition = MessageReOrder.insert(Dposition, CharD)

        try:
            for CountCharD in range(0, MessageCount):
                Aposition = MessageSplit.index('d')
                OutputTotal += 8
                RMposition =  MessageSplit.remove(Dposition)
                INTposition =  MessageReOrder.insert(Dposition, CharD)
        except:
            print("only one d found")

            print(MessageReOrder)

    if 'e' in MessageSplit:
        CountCharE = MessageSplit.count('e')
        Eposition = MessageSplit.index('e')    
        print(Eposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Eposition] #new method

        OutputTotal += 2
        INTposition = MessageReOrder.insert(Eposition, CharE)

        try:
            for CountCharE in range(0, MessageCount):
                Eposition = MessageSplit.index('e')
                OutputTotal += 2
                RMposition =  MessageSplit.remove(Eposition)
                INTposition =  MessageReOrder.insert(Eposition, CharE)
        except:
            print("only one e found")

            print(MessageReOrder)





   

    else:
        print('either you have not input a character,interger or symbol')
        sys.exit()
            
            
            
    MessageReOrder.reverse()
    
    print(MessageReOrder)
    print("flipped")
    

    MessageReOrder.insert(0, 'x')
    INToutput = MessageReOrder.insert(0,OutputTotal)
    print("with output total")
    print(MessageReOrder)
    
    #get rid of all speech marks
    
    
    SpeechCount = MessageReOrder.count(" \" \" ")    

    for SpeechCount in range(0, SpeechCount):
        MessageReOrder.remove(" \" \" ")
        

    
    
    print(MessageReOrder)

    result = ' '.join(map(str, MessageReOrder))

    f = open('MessageOutput.txt' , 'w')
    f.write('Encoded messsage\n')
    f.write (str(MessageReOrder))
    f.write('\nUnEncoded messsage\n')
    f.write(TestMessage)
    f.write('\nUnlisted message\n')
    f.write(result)

    f.close()



    

    

    

EncodingBase()
    

