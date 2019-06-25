#ifndef TEA_H
#define TEA_H

#define TEA_DECRYPT     0
#define TEA_ENCRYPT     1
#define XTEA_DECRYPT    2
#define XTEA_ENCRYPT    3

int crypt(unsigned long* data, unsigned long* key, int len, int mode);

#endif