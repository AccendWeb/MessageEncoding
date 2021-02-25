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
TestMessage = "wap"

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

    if 'w' in MessageSplit:
        CountCharW = MessageSplit.count('w')
        Wposition = MessageSplit.index('w')    
        print(Wposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Wposition] #new method

        OutputTotal += 46
        INTposition = MessageReOrder.insert(Wposition, CharW)

        try:
            for CountCharW in range(0, MessageCount):
                Wposition = MessageSplit.index('w')
                OutputTotal += 46
                RMposition =  MessageSplit.remove(Wposition)
                INTposition =  MessageReOrder.insert(Wposition, CharW)
        except:
            print("only one W found")

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
            
            
    
    
    
    if 'p' in MessageSplit:
        CountCharP = MessageSplit.count('p')
        Pposition = MessageSplit.index('p')    
        print(Aposition)
      
      #old method but keep for later
      # RMposition = MessageSplit.remove(Wposition, CharW)

        del MessageSplit[Aposition] #new method

        OutputTotal += 32
        INTposition = MessageReOrder.insert(Aposition, CharP)

        try:
            for CountCharP in range(0, MessageCount):
                Aposition = MessageSplit.index('p')
                OutputTotal += 32
                RMposition =  MessageSplit.remove(Pposition)
                INTposition =  MessageReOrder.insert(Pposition, CharP)
        except:
            print("only one p found")

            print(MessageReOrder)
            print("unflipped\n")
            
            
            
            
    MessageReOrder.reverse()
    
    print(MessageReOrder)
    print("flipped")
    
    INToutput = MessageReOrder.insert(0,OutputTotal)
    print("with output total")
    print(MessageReOrder)
    
    #get rid of all speech marks
    
    
    SpeechCount = MessageReOrder.count(" \" \" ")    

    for SpeechCount in range(0, SpeechCount):
        MessageReOrder.remove(" \" \" ")
        
    print(MessageReOrder)

    f = open('MessageOutput.txt' , 'w')
    f.write('Encoded\n')
    f.write (str(MessageReOrder))

    f.close()

    

    

    

EncodingBase()
    

