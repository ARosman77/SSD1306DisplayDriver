
import oled

oled.init(0,0x3C)
oled.sendCmd(0xA4)
oled.sendCmd(0xD3,0x00,0x10)
oled.sendData(0x01,0x02,0x04,0x08,0x10)