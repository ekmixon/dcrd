import sys
from ed25519 import *

x = int(sys.argv[1])
y = int(sys.argv[2])
P = [x, y]
encodepointhex(P)
