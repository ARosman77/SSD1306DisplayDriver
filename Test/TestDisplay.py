"""
SSD 1306 Display i2c communication test

"""

import time
import os
from pyA20 import i2c

display_address = 0x3C

# Initialize i2c bus
i2c.init("/dev/i2c-0")
i2c.open(display_address)

# set position
def setInitPos():
    """ Put cursor to initial position """
    i2c.write([0x80,0x21])
    i2c.write([0x80,0])
    i2c.write([0x80,127])

    i2c.write([0x80,0x22])
    i2c.write([0x80,0])
    i2c.write([0x80,7])
    return

# Init Display
# Turn Charge Pump ON
i2c.write([0x80,0x8D])
i2c.write([0x80,0x14])
# Turn Display On
i2c.write([0x80,0xAF])

# Set display mapping
i2c.write([0x80,0xA6])
i2c.write([0x80,0xA4])
i2c.write([0x80,0xA1])
i2c.write([0x80,0xC8])
i2c.write([0x80,0xD3])
i2c.write([0x80,63-16]) # skip 2 pages of yellow display

# set addressing mode
i2c.write([0x80,0x20])
i2c.write([0x80,0x00])

setInitPos()

# clear display
for page in range(0,8):
    for col in range(0, 128):
        i2c.write([0x40,0x00])

setInitPos()

# try to write something
#i2c.write([0x40,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80])
i2c.write([0x40,0x00,0x00,0xE7,0x84,0x43,0x20,0x00,0x00])
i2c.write([0x40,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
i2c.write([0x40,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80])

# End of Test (wait 5s before clean-up)
time.sleep(5)
# Turn Display Off
i2c.write([0x80,0xAE])
# Close I2C bus
i2c.close()
