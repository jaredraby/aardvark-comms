import cmd, sys
from aardvark_py import *

class AardvarkShell(cmd.Cmd):
    intro = 'Welcome to the Aardvark Shell. Type help or ? to list commands.\n'
    prompt = '(aardvark) '
    file = None

    # ------- basic aardvark commands ------
    def do_findaardvark(self,arg):
        'Scan for attached aardvarks, return ID and status if any'

    def do_setMode(self,arg):
        'Set the aardvark for i2c or spi communications'

    # ------- basic i2c commands ------
    def do_i2cSetBitRate(self,arg):
        'Set the bitrate for the i2c bus. X, Y, Z allowed.'

    # ------- basic spi commands ------
    def do_spiSetBitRate(self,arg):
        'Sit the bitrate for the i2c bus. A, B, C allowed.'


if __name__ == '__main__':
    AardvarkShell().cmdloop()