/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "blowfish.h"

void usage()
{
	printf("Usage: blowfish [-e(encrypt)|-d(decrypt)]\n");
}

int input_hex_1byte(uint8_t* inbuf, const char* hint)
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

int input_hex_4bytes(uint32_t* inbuf, const char* hint)
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

void crypt(int is_encrypt)
{
  BLOWFISH_CTX ctx;
  uint32_t data[8 * 1024];
  uint8_t key[60]; //max: 448bit=56byte
  int i, len;

  memset(data, 0, sizeof(data));
  memset(key, 0, sizeof(key));
  len = input_hex_1byte(key, "key");
  Blowfish_Init(&ctx, key, len);
  
  len = input_hex_4bytes(data, is_encrypt ? "plaintext" : "ciphertext");
  
  printf("\n%s(in hex) is: ", is_encrypt ? "cipher" : "plain");
  for (i = 0; i < len; i += 2) {
    if (is_encrypt)
      Blowfish_Encrypt(&ctx, &data[i], &data[i+1]);
    else
      Blowfish_Decrypt(&ctx, &data[i], &data[i+1]);
    printf("%08x%08x", data[i], data[i+1]);
  }
  
}

int main(int argc, char **argv)
{
  int is_encrypt;
  if(argc < 2 || argv[1][0] != '-')
	{
		usage();
		return 1;
	}
  
	switch(argv[1][1])
	{
		case 'e':
		case 'E':
      is_encrypt = 1;
			break;
    case 'd':
		case 'D':
      is_encrypt = 0;
			break;
		default:
			usage();
			return 1;
	}
  crypt(is_encrypt);
  
	return 0;
}