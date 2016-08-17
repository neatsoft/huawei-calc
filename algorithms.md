##1

    #!/usr/bin/env python

    import hashlib
    import humod
    UNLOCK_SALT = "5e8dd316726b0335"

    def show_code(imei, salt):
        digest = hashlib.md5((imei+salt).lower()).digest()
        code = 0
        for i in range(0,4):
            code += (ord(digest[i])^ord(digest[4+i])^ord(digest[8+i])^ord(digest[12+i])) << (3-i)*8
            code &= 0x1ffffff
            code |= 0x2000000
        return code

    mod = humod.Modem()
    imei = mod.show_imei()
    status = humod.at_commands.Command(mod,'AT^CARDLOCK="'+str(show_code(imei,UNLOCK_SALT))+'"\r')

##2

    #!/usr/bin/env python

    import hashlib
    UNLOCK_SALT = "5e8dd316726b0335"

    def show_codes(imei, salt):
        digest = hashlib.md5((imei+salt).lower()).digest()
        code = 0
        for i in range(0,4):
            code += (ord(digest[i])^ord(digest[4+i])^ord(digest[8+i])^ord(digest[12+i])) << (3-i)*8
            code &= 0x1ffffff
            code |= 0x2000000
        return code

    # PLEASE TYPE YOUR IMEI  BELOW
    imei = ' '
    if(imei == ' '):
        print 'Please open this script from your editor and enter your IMEI'
    else:
        print "Your Modem unlock code: %s" % show_codes(imei,UNLOCK_SALT);

##3

    cat /dev/ttyUSB0 &
    echo -e “ATI\r” > /dev/ttyUSB0
    echo -e 'AT^CARDLOCK="XXXXXXXX"\r' > /dev/ttyUSB0
