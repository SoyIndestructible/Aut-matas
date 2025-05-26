import sys
import time
from ejemploFAdo_IPV4 import *

def main() -> int:
    evaluar()
    return

if __name__=='__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pritn("\n *** F I N ***")
        sys.exit(0)
