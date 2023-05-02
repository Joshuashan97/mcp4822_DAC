from spidriver import SPIDriver
import sys


s = SPIDriver("COM34")


configbits = 3
data1 = (configbits<<4) + 0
data2 = int(sys.argv[1])

#print(type(int(sys.argv[1])))
#print(type((sys.argv[1])))
s.seta(1)
s.sel()
s.write([data1])
s.write([data2])
s.unsel()
s.seta(0)

print(bin((data1<<8)+data2))

exit