//#include <stdint.h>
#include <string.h>
#include "tea.h"

#define ROUNDS 32
#define DELTA 0x9e3779b9 /* sqr(5)-1 * 2^31 */

void tea_encrypt_block (unsigned long* v, unsigned long* k) {
    unsigned long v0=v[0], v1=v[1], sum=0, i;           /* set up */
    unsigned long k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i < ROUNDS; i++) {                       /* basic cycle start */
        sum += DELTA;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);  
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}
 
void tea_decrypt_block (unsigned long* v, unsigned long* k) {
    unsigned long v0=v[0], v1=v[1], sum=DELTA << 5, i;  /* set up DELTA * 2**32 = 0xC6EF3720*/
    unsigned long k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i<ROUNDS; i++) {                         /* basic cycle start */
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= DELTA;                                   
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

void xtea_encrypt_block(unsigned long* v, unsigned long* k) {
    unsigned int i;
    unsigned long v0=v[0], v1=v[1], sum=0;
    for (i=0; i < ROUNDS; i++) {
        v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + k[sum & 3]);
        sum += DELTA;
        v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + k[(sum>>11) & 3]);
    }
    v[0]=v0; v[1]=v1;
}
 
void xtea_decrypt_block(unsigned long* v, unsigned long* k) {
    unsigned int i;
    unsigned long v0=v[0], v1=v[1], sum=DELTA << 5;
    for (i=0; i < ROUNDS; i++) {
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + k[(sum>>11) & 3]);
        sum -= DELTA;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + k[sum & 3]);
    }
    v[0]=v0; v[1]=v1;
}

int crypt(unsigned long* data, unsigned long* key, int len, int mode) {
  int i;
  for (i = 0; i < len; i += 2) {
    switch (mode){
    case TEA_ENCRYPT:
      tea_encrypt_block(&data[i], key);
      break;
    case TEA_DECRYPT:
      tea_decrypt_block(&data[i], key);
      break;
    case XTEA_ENCRYPT:
      xtea_encrypt_block(&data[i], key);
      break;
    case XTEA_DECRYPT:
      xtea_decrypt_block(&data[i], key);
      break;
    }
  }
  return len;
}