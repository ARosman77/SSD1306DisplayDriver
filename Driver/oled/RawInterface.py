"""

Low level comunication with oled display

"""

from pyA20 import i2c

def init(interface,addr):
    """ Initalize i2c interface """
    print "Init communication on i2c-"+str(interface)+" and address "+str(addr)+"."
    # Initialize i2c bus
    i2c.init("/dev/i2c-"+str(interface))
    i2c.open(addr)

def sendCmd(cmd,*args):
    """ send command to oled display """
    # TODO:optimize to one i2c write if possible
    i2c.write([0x80,cmd])
    for arg in args:
        i2c.write([0x80,arg])

def sendData(data, *moreData):
    """ send data to oled RAM """
    output = [0x40,data]
    for mData in moreData:
        output.append(mData)
    i2c.write(output)
