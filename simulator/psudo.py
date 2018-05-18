#Text display

#16 Bit words

#| 4 Instruction | 12 Data |
#0x00 0000
#0x01 0000
#0x02 0000
#0x03 0000
# ...

#Registers

#   General
# $I - Instruction Counter(0x00)
# $A - Gen Comp
# $B - Gen Comp

#   Screen
# $SX - X Cursor
# $SY - Y Cursor
# $SC - Draw Color
# $ST - Text to draw

#Read Address I

#   Instructions
# MV d r - Move d into register r
# *JMP d - Move int d into $i
# ....

#Color Format
#RGB_
