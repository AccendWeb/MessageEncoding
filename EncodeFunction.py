import sys
import subprocess 
import time 
import os 
import re 
import array 

#------------ TO-DO --------------

#First start with encoding before decoding
#Make a function to read the string/message
#make sure the output is correct 
#show total output in terminal/debug
#add total counter 

#---------------------------------

#declare all base 2 characters

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

#--------------testing----------------
TestMessage = "w"

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
   
   if 'w' in MessageSplit:
        CountCharW = MessageSplit.count('w')
        Wposition = MessageSplit.index('w')    
        print(Wposition)
        MessageSplit.remove[Wposition]
        OutputTotal += 48
        MessageReOrder.insert(Wposition, CharW)
       
        for CountCharW in MessageCount:
            Wposition = MessageSplit.index('w')
            OutputTotal += 48
            MessageSplit.remove(Wposition)
            MessageReOrder.insert(Wposition, CharW)





    if 'a' in MessageSplit:
        CountCharW = MessageSplit.count('w')
        OutputMessage.append(CharW)
        OutputMessage.append(1)
        OutputTotal += 48
        print(OutputMessage)
        print(OutputTotal)
        print(CountCharW, "number of characters in string/word")

    if 'w' in MessageSplit:
        CountCharW = MessageSplit.count('w')
        OutputMessage.append(CharW)
        OutputMessage.append(1)
        OutputTotal += 48
        print(OutputMessage)
        print(OutputTotal)
        print(CountCharW, "number of characters in string/word")


   



    
EncodingBase()
    

