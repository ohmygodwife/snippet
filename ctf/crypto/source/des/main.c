/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "des.h"

void usage()
{
	printf("Usage: des [-e(des encrypt)|-d(des decrypt)|-t(3des encrypt)|-s(3des decrypt)]\n");
}

int input_hex_1byte(const unsigned char* inbuf, const char* hint)
{
  char str[8 * 1024 * 2];
  int len = 0;
  
  printf("\ninput %s(in hex):", hint);
	scanf("%s", str);
  
  while(sscanf(str+len*2, "%02x", &(inbuf[len]))!=EOF)
		len++;
  
  printf("debug: %i, %s, %s\n", len, str, inbuf);
  return len;
}

int input_hex_4bytes(const unsigned long* inbuf, const char* hint)
{
  char str[8 * 1024 * 2];
  char tmp[1024];
  int len = 0;
  
  printf("\ninput %s(in hex):", hint);
	scanf("%s", str);
  len = strlen(str);
	for(; len%16 != 0; len++)
		str[len] = '0';
	str[len] = '\0';
  len = 0;
  
//  while (sscanf(str+len*2, "%08x", &(tmp[len]))!=EOF)
//    len += 4;
  while(sscanf(str+len*8, "%08x", &(inbuf[len]))!=EOF)
		len++;
  
//  printf("debug: %i, %s, %s\n", len, str, tmp);
  printf("debug: %i, %s, %s\n", len, str, inbuf);
  return len;
}

void output_hex_1byte(const unsigned char *outbuf, int len, const char* hint)
{
  int i;
  printf("\n%s(in hex) is: ", hint);
  for(i = 0; i < len; i++)
	{
		printf("%02x", outbuf[i]);
	}
  printf("\n%s text is: %s", hint, outbuf);
}

void des_crypt(int is_decrypt)
{
  des_ctx ctx;
  unsigned char inbuf[8 * 1024];
  unsigned char outbuf[8 * 1024];
  unsigned char key[8];
  int i, len;

  memset(inbuf, 0, sizeof(inbuf));
  memset(outbuf, 0, sizeof(outbuf));
  memset(key, 0, sizeof(key));
  len = input_hex_1byte(key, "key");
  des_setkey(ctx, key);
  
  len = input_hex_1byte(inbuf, is_decrypt ? "ciphertext" : "plaintext");
  
  for (i = 0; i < len; i += 8) {
    if (is_decrypt)
      des_ecb_decrypt(ctx, &inbuf[i], &outbuf[i]);
    else
      des_ecb_encrypt(ctx, &inbuf[i], &outbuf[i]);
  }
  output_hex_1byte(outbuf, len, is_decrypt ? "plain" : "cipher");
}

void triple_des_crypt(int is_decrypt)
{
  tripledes_ctx ctx;
  unsigned char inbuf[8 * 1024];
  unsigned char outbuf[8 * 1024];
  unsigned char key[8 * 3];
  int i, len;

  memset(inbuf, 0, sizeof(inbuf));
  memset(outbuf, 0, sizeof(outbuf));
  memset(key, 0, sizeof(key));
  len = input_hex_1byte(key, "key");
  tripledes_set3keys(ctx, key, key+8, key+16);
  
  len = input_hex_1byte(inbuf, is_decrypt ? "ciphertext" : "plaintext");
  
  for (i = 0; i < len; i += 8) {
    if (is_decrypt)
      tripledes_ecb_decrypt(ctx, &inbuf[i], &outbuf[i]);
    else
      tripledes_ecb_encrypt(ctx, &inbuf[i], &outbuf[i]);
  }
  output_hex_1byte(outbuf, len, is_decrypt ? "plain" : "cipher");
}

int main(int argc, char **argv)
{
  if(argc < 2 || argv[1][0] != '-')
	{
		usage();
		return 1;
	}
  
	switch(argv[1][1])
	{
		case 'e':
		case 'E':
      des_crypt(0);
			break;
    case 'd':
		case 'D':
      des_crypt(1);
			break;
    case 't':
		case 'T':
      triple_des_crypt(0);
			break;
    case 's':
		case 'S':
      triple_des_crypt(1);
			break;
		default:
			usage();
			return 1;
	}
  
	return 0;
}