
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

# internal functions
def print8pt(str):
	""" Print on display at current position with 8pt fonts """
	for idx, char in enumerate(str):
		# allow only 21 characters per line, discard the rest
		if (idx)>20: break
		pos=(ord(char)-32)*5
		sendDataL(Font_8pt[pos:pos+5])
		# Send Space between characters
		sendData(0x00)

def print12pt(str):
	""" Print on display at current position with 12pt fonts """
	for idx, char in enumerate(str):
			# allow only 14 characters per line, discard the rest
			if (x+idx)>13: break
			pos=(ord(char)-32)*18
			data=swapNibbles(Font_12pt[pos:pos+18])
			sendDataL(data)

def printAt(str,line=0,col=0,clearLn=0,bigFont=0):
	""" Print function that covers all possibilities """
	# choose correct mode, depending on bigFont
	if bigFont > 0:
		setDispMode(bigFont)
		maxLine = 3
		maxCol = 13
	else:
		setDispMode(bigFont)
		maxLine = 7
		maxCol = 20
	# validate parameters
	if line < 0 : line = 0
	if line > maxLine : line = maxLine
	if col < 0 : col = 0
	if col > maxCol : col = maxCol
	# clear the line if requested
	if clearLn > 0:
		clearLn(line,bigFont)
	# go to specified position
	setPos(line,col,bigFont)
	# transform string to correct length so it doesn't overflow
	allowedLen = maxCol-col
	# call correct print function, depending on bigFont
	if bigFont > 0 : print12pt(str[:allowedLen])
	else : print8pt(str[:allowedLen])

def swapNibbles(list):
    """ Swap nibbles of font data """
    for i in range(0,len(list),2):
        list[i],list[i+1]=list[i+1],list[i]
    return list

# exported test function (delete when merging with master)
def testDispFn():
		""" Test function """
		printAt("HW",line=0,col=0,clearLn=0,bigFont=0)
		return 0

# exported functions
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
		#cut the string, and call function
    for idx, char in enumerate(str):
        # allow only 14 characters per line, discard the rest
        if (x+idx)>13: break
        pos=(ord(char)-32)*18
        data=swapNibbles(Font_12pt[pos:pos+18])
        sendDataL(data)

def printBluLnBig(str,y=0,x=0):
    """ Print string at line y, position x, on blue part of display with big fonts """
    # Check for valid parameters
    if y<0: y=0
    if y>3: y=3
    if x>13: x=13
    # Clear whole line
    clearBluLnBig(y)
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

def clearBluLnBig(line):
    cmdSetAddrMode(ADDR_MODE_VER)
    cmdSetColAddr(0,127)
    cmdSetPageAddr(line*2,line*2+1)
    cmdSetCurCol(0)
    clearData = [0]*128
    sendDataL(clearData)
    sendDataL(clearData)
