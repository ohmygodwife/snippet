/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "tea.h"

void usage()
{
	printf("Usage: tea [-e(tea encrypt)|-d(tea decrypt)|-x(xtea encrypt)|-t(xtea decrypt)]\n");
}

int input_hex_4bytes(unsigned long* inbuf, const char* hint)
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

void output_hex_4bytes(unsigned long *outbuf, int len, const char* hint)
{
  int i;
  printf("\n%s(in hex) is: ", hint);
  for(i = 0; i < len; i++)
	{
		printf("%08x ", outbuf[i]);
	}
}

int main(int argc, char **argv)
{
  unsigned long data[8 * 1024];
  unsigned long key[16];
  int is_encrypt, mode, len;
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
			mode = TEA_ENCRYPT;
			break;
    case 'd':
		case 'D':
      is_encrypt = 0;
			mode = TEA_DECRYPT;
			break;
    case 'x':
		case 'X':
      is_encrypt = 1;
			mode = XTEA_ENCRYPT;
			break;
    case 't':
		case 'T':
      is_encrypt = 0;
			mode = XTEA_DECRYPT;
			break;
		default:
			usage();
			return 1;
	}
  memset(data, 0, sizeof(data));
  input_hex_4bytes(key, "key");
  len = input_hex_4bytes(data, is_encrypt ? "plaintext" : "ciphertext");
  crypt(data, key, len, mode);
  output_hex_4bytes(data, len, is_encrypt ? "cipher" : "plain");
  
	return 0;
}