// Huawei unlock codes calculator
// based on https://github.com/forth32/huaweicalc
// compile: g++ huawei-calc.cpp -L/usr/lib -lssl -lcrypto -o huawei-calc

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

void encrypt_v1(char* imei, char* resbuf, char* hstr) {
    unsigned char xbytes[17];
    char ybytes[100];
    char hash[100];
    unsigned int rh[30];
    unsigned char res[4];
    int i;

    memset(xbytes,0,17);
    MD5((unsigned char*)hstr, strlen(hstr), xbytes);

    for(i = 0; i < 16; i++)
        sprintf(ybytes + (i * 2), "%02x", xbytes[i] & 0xff);

    strcpy(hash, imei);
    strncat(hash, ybytes + 8, 16);
    hash[31] = 0;
    MD5((unsigned char*)hash, 31, xbytes);

    for (i = 0; i < 16; i++)
        rh[i] = xbytes[i] & 0xff;

    for(i = 0; i < 4; i++)
        res[3-i] = rh[i] ^ rh[i+4] ^ rh[i+8] ^ rh[i+12];

    i=*((unsigned int*)&res);
    i |= 0x2000000;
    i &= 0x3FFFFFF;

    sprintf(resbuf, "%i", i);
}

int main(int argc, char* argv[]) {
    char codebuf[40];
    char imeibuf[16];

    if (argc != 2) {
        printf("usage: %s <IMEI>\n", basename(argv[0]));
        return EXIT_FAILURE;
    }

    if (strlen(argv[1]) != 15) {
        printf("error: IMEI should contain 15 digits\n");
        return EXIT_FAILURE;
    }

    strncpy(imeibuf, argv[1], 15);

    printf("  IMEI              = %s\n", imeibuf);

    encrypt_v1(imeibuf, codebuf, "hwe620datacard");
    printf("  Unlock code       = %s\n", codebuf);

    encrypt_v1(imeibuf, codebuf, "e630upgrade");
    printf("  Flash code        = %s\n", codebuf);

    return EXIT_SUCCESS;
}
