
""" User commands for oled display """

from RawInterface import sendDataL
from RawInterface import sendData
from DisplayCommands import cmdSetColAddr
from DisplayCommands import cmdSetPageAddr
from DisplayCommands import cmdSetCurPage
from DisplayCommands import cmdSetCurCol
from DisplayCommands import cmdSetAddrMode
from DisplayCommands import ADDR_MODE_PAGE
from DisplayCommands import ADDR_MODE_VER
from fonts import Font_8pt
from fonts import Font_12pt

def swapNibbles(list):
    """ Swap nibbles of font data """
    for i in range(0,len(list),2):
        list[i],list[i+1]=list[i+1],list[i]
    return list

def printYelLn(str,x=0):
    """ Print string at position x on yellow part of display """
    # Check for valid parameters
    if x>13: x=13
    # Clear whole line
    clearYelLn()
    # set correct mode
    #cmdSetAddrMode(ADDR_MODE_VER)
    #cmdSetColAddr(0,127)
    #cmdSetPageAddr(0,1)
    cmdSetCurCol(9*x)
    for idx, char in enumerate(str):
        # allow only 14 characters per line, discard the rest
        if (x+idx)>13: break
        pos=(ord(char)-32)*18
        data=swapNibbles(Font_12pt[pos:pos+18])
        sendDataL(data)

def printBluLn(str,y=0,x=0):
    """ Print string at line y, position x, on blue part of display """
    # Check for valid parameters
    if y<0: y=0
    if y>5: y=5
    if x>20: x=20
    # Clear whole line
    clearBluLn(y)
    # Following commands already sent by clearBluLn
    #cmdSetColAddr(0,127)
    #cmdSetPageAddr(2,7)
    #cmdSetCurPage(2+y)
    #cmdSetAddrMode(ADDR_MODE_PAGE)
    cmdSetCurCol(6*x)
    for idx, char in enumerate(str):
        # allow only 21 characters per line, discard the rest
        if (x+idx)>20: break
        pos=(ord(char)-32)*5
        sendDataL(Font_8pt[pos:pos+5])
        sendData(0x00)

def clearBluLn(line):
    # Check for valid parameters
    if line<0: line=0
    if line>5: line=5
    cmdSetColAddr(0,127)
    cmdSetPageAddr(2,7)
    cmdSetCurPage(2+line)
    cmdSetCurCol(0)
    cmdSetAddrMode(ADDR_MODE_PAGE)
    clearData = [0]*128
    sendDataL(clearData)

def clearYelLn():
    cmdSetAddrMode(ADDR_MODE_VER)
    cmdSetColAddr(0,127)
    cmdSetPageAddr(0,1)
    cmdSetCurCol(0)
    clearData = [0]*128
    sendDataL(clearData)
    sendDataL(clearData)
