"""

Low level comunication with oled display

"""

from pyA20 import i2c

def init(interface,addr):
    print "Init communication on i2c-"+str(interface)+" and address "+str(addr)+"."

def sendCmd(cmd,*args):
    """ send command to oled display """
    print cmd
    for arg in args:
        print arg

def sendData(data, *moreData):
    """ send data to oled RAM """
    print data
    for mData in moreData:
        print mData
