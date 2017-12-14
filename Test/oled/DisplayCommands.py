
""" Constants """
ADDR_MODE_HOR = 0x00
ADDR_MODE_VER = 0x01
ADDR_MODE_PAGE = 0x02

""" Display commands """

from RawInterface import sendCmd 

def cmdSetContrast(contrast):
    """ Set display contrast 0-255 """
    if contrast>255: raise ValueError('Paramteres from 0 to 255 excepted!')
    sendCmd(0x81,contrast)

def cmdDisplayON():
    """ Turn display on """
    sendCmd(0xAF)

def cmdDisplayOFF():
    """ Turn display off """
    sendCmd(0xAE)

def cmdDisplayAllOn(bOn):
    """ Turn all pixels On """
    if bOn: sendCmd(0xA5)
    else: sendCmd(0xA4)

def cmdDisplayInverse(bInverse):
    """ Inverse display """
    if bInverse: sendCmd(0xA7)
    else: sendCmd(0xA6)

def cmdSetAddrMode(addrMode):
    """ Set display address mode """
    if addrMode == ADDR_MODE_HOR or ADDR_MODE_VER or ADDR_MODE_PAGE:
        sendCmd(0x20,addrMode)
    else:
        raise ValueError("Undefined address mode!")

def cmdSetCurPage(page):
    """ Set Page Start Address, Current Line if in Page Mode """
    if (page<0) or (page>7):
        raise ValueError("Pages from 0 to 7 supported!")
    sendCmd(0xB0 | page)

def cmdSetCurCol(col):
    """ Set Column Start Address, Current column in Page Mode """
    if (col<0) or (col>127):
        raise ValueError("Columns from 0 to 127 supported!")
    sendCmd(col & 0x0F)                     # lower nibble with cmd 0x00
    sendCmd(((col >> 4) & 0x0F) | 0x10 )    # higher nibble with cmd 0x01

def cmdChargePumpEnable():
    """ Enable charge pump for the display """
    sendCmd(0x8D,0x14)

def cmdChargePumpDisable():
    """ Disable charge pump for the display """
    sendCmd(0x8D,0x10)

def cmdSetStartRow(startRow):
    """ Set Display RAM start row from 0-63 """
    if (startRow<0) or (startRow>63):
        raise ValueError("Start Row from 0 to 63 supported!")
    sendCmd(0x40 | startRow)

def cmdRemapCol(bRemap):
    """ Remap segments to either start from 0 or from 127 """
    if bRemap: sendCmd(0xA1)
    else: sendCmd(0xA0)

def cmdSetMuxRatio(muxRatio):
    """ Set MUX ratio to N+1 MUX, values from 16 to 63 allowed """
    if (muxRatio<15) or (muxRatio>63):
        raise ValueError("Mux Ratio from 16 to 63 supported!")
    sendCmd(0xA8,muxRatio)

def cmdRemapRow(bRemap):
    """ Remap COM Output scan direction """
    if bRemap: sendCmd(0xC8)
    else: sendCmd(0xC0)

def cmdSetRowOffset(offset):
    """ Set vertical shift by COM from 0 to 63 """
    if (offset<0) or (offset>63):
        raise ValueError("Offset from 0 to 63 supported!")
    sendCmd(0xD3,offset)

