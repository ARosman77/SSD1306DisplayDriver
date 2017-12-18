#!/usr/bin/env python
""" Set display contrast to low value  """
import oled

oled.init(0,0x3C)
oled.cmdDisplayON()
oled.cmdSetContrast(1)
