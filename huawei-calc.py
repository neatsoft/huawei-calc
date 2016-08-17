#!/usr/bin/python
# -*- coding: utf-8 -*-
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the
#      Free Software Foundation, Inc.,
#      59 Temple Place, Suite 330,
#      Boston, MA  02111-1307  USA
#
#   Copyright 2010 Gunslinger_ <yudha.gunslinger@gmail.com>
#   http://bit.ly/c0debreaker
 
import hashlib, string
 
__author__  = "Gunslinger_ <yudha.gunslinger@gmail.com>"
__date__    = "Tue, 14 Jun 2011 23:22:42 +0700"
__version__     = "1.0"
__copyright__   = "Copyright (c) 2010 Gunslinger_"
 
class huawei_modem_unlocker(object):
    """
    Instance variables:
 
    Imei
        Imei of the modem will be calculated
        Default : '0'
 
    Verbose
        Display how algorithm working
        Default : False
 
    """
    def __init__(self, imei='0', verbose=False):
        ''' Huawei modem unlocker class constructor '''
        self._imei      = imei
        self._verbose       = verbose
        self._md5u      = hashlib.md5(str(imei)+str('5e8dd316726b0335')).hexdigest()
        self._md5f      = hashlib.md5(str(imei)+str('97b7bc6be525ab44')).hexdigest()
        self._unlock_code   = ''
        self._flash_code    = ''
        # verbose formating
        self._width     = 21
        self._w         = 10
        self._header_format     = '%-*s%*s'
        self._format        = '   %d  | %-*s | %*s  '
 
    def xor_digits(self, source, counter):
        ''' Get a value and xoring it during looping iteration '''
        digits = int('0x0'+source[0+counter:2+counter],16)  ^ \
             int('0x0'+source[8+counter:8+2+counter],16)    ^ \
             int('0x0'+source[16+counter:16+2+counter],16)  ^ \
             int('0x0'+source[24+counter:24+2+counter],16)
        return digits
 
    def calc(self):
        ''' Process calculate with the algorithm (read source code) '''
        cnt = 0
        cnt2 = 1
        if self._verbose:
            print "="*(self._width+13)
            print " Iter."+"|"+ " Unlock byte "+"|"+" Flash byte "
            print "-"*(self._width+13)
        while cnt < 8:
            digits_unlock   = self.xor_digits(self._md5u, cnt)
            digits_flash    = self.xor_digits(self._md5f, cnt)
            unlock_byte     = string.zfill(hex(digits_unlock)[2:],2)
            flash_byte  = string.zfill(hex(digits_flash)[2:],2)
            self._unlock_code = str(self._unlock_code)+str(unlock_byte)
            self._flash_code  = str(self._flash_code)+str(flash_byte)
            if self._verbose: print self._format % (int(cnt2), self._width - self._w, self._unlock_code , self._w, self._flash_code)
            cnt  +=2
            cnt2 +=1
        if self._verbose:
            print "="*(self._width+13)
            print "\nUNLOCK CODE = %d & %d | %d = %d" % (int('0x0'+self._unlock_code,16), 33554431, 33554432, eval("int('0x0'+self._unlock_code,16) & 33554431 | 33554432"))
            print "FLASH CODE  = %d & %d | %d = %d\n" % (int('0x0'+self._flash_code,16), 33554431, 33554432, eval("int('0x0'+self._flash_code,16) & 33554431 | 33554432"))
        self._unlock_code   = int('0x0'+self._unlock_code,16) & 33554431 | 33554432
        self._flash_code    = int('0x0'+self._flash_code,16) & 33554431 | 33554432
        return (self._unlock_code, self._flash_code)
 
    def run(self):
        ''' Fire it up ! '''
        self.calc()
        return (self._unlock_code, self._flash_code)
 
if __name__ == '__main__':
    print "\nHuawei modem unlock code calculator v.%s by %s \n" % (__version__, __author__)
    inpimei = raw_input("Please input modem IMEI : ")
    cracker = huawei_modem_unlocker(inpimei)
    a, b    = cracker.run()
    print "\n-> IMEI     = %s" % (inpimei)
    print "-> UNLOCK CODE    = %s" % (a)
    print "-> FLASH CODE = %s" % (b)
