#!/usr/bin/env python
""" Turn Display OFF """
import oled

oled.init(0,0x3C)

oled.cmdDisplayOFF()
