#Huawei unlock codes calculators

##Supported devices
- E1550
- E171

##Possibly supported (not tested)
- other E-based Huawei modems

##How to check IMEI

    minicom -D /dev/ttyUSB0
    ATZ
    ATI

##How to check cardlock status

    minicom -D /dev/ttyUSB0
    ATZ
    AT^CARDLOCK?

####Return codes:

#####Locked:

    ^CARDLOCK: 1,10,0

#####Unlocked:

    ^CARDLOCK: 2,10,0

##How to unlock modem

    minicom -D /dev/ttyUSB0
    ATZ
    AT^CARDLOCK="UNLOCK_CODE"

##Links

[Huawei E1550 3G modem (arch wiki)](https://wiki.archlinux.org/index.php/Huawei_E1550_3G_modem)

[Huawei modem unlock code calculator (cpp) (rus)](https://github.com/forth32/huaweicalc)

[Huawei modem unlock calculator (python)](https://c0debreaker.com/tag/command-line/)

[Unlocking a Huawei 3G Modem, use it on multiple networks (python code)](https://zenu.wordpress.com/2011/05/19/unlocking-3g-modems-and-using-them-on-other-networks/)

[Разлочка Huawei модемов (rus)](http://blog.angel2s2.ru/2010/07/huawei.html)

[Online huawei modem unlock code calculator](http://a-zgsm.com/freecode/huawei/submit/)

[Linux + Huawei E1550 (AT commands) (rus)](http://galaober.org.ua/node/73)
