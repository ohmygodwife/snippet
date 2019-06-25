/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "aes.h"
#define MAX_SIZE 16 * 1024

void usage()
{
	printf("Usage: sm4 [-e(encrypt)|-d(decrypt)|-c(cbc_encrypt)|-b(cdc_decrypt)]\n");
}

struct AES_ctx ctx;
unsigned char iv[AES_BLOCKLEN];
void read_iv()
{
  char str[40];
  int i;
  printf("\ninput 128-bit initial value(in hex):");
	scanf("%s", str);
  for(i = 0; i < AES_BLOCKLEN; i++)
    sscanf(str+i*2, "%02x", &iv[i]);
}

#define PLAIN_STR "plain"
#define CIPHER_STR "cipher"

void crypt(int is_decrypt, int is_iv)
{
	unsigned char key[AES_KEYLEN];
  unsigned char input[MAX_SIZE];
  char str[MAX_SIZE * 2];
  int len = 0, i;
  
  memset(input, 0, MAX_SIZE);
  
  printf("\ninput %stext(in hex):", is_decrypt ? CIPHER_STR : PLAIN_STR);
  scanf("%s", str);
	while(sscanf(str+len*2, "%02x", &(input[len]))!=EOF)
		len++;
  
  printf("\ninput 128-bit secret key(in hex):");
	scanf("%s", str);
  for(i = 0; i < AES_BLOCKLEN; i++)
		sscanf(str+i*2, "%02x", &key[i]);
    
  //encrypt standard testing vector
  AES_init_ctx(&ctx, key);
  
  if (is_iv) {
    AES_ctx_set_iv(&ctx, iv);
    if (is_decrypt)
      AES_CBC_decrypt_buffer(&ctx, input, len);
    else
      AES_CBC_encrypt_buffer(&ctx, input, len);
  } else {
    if (is_decrypt)
      AES_ECB_decrypt(&ctx, input, len);
    else
      AES_ECB_encrypt(&ctx, input, len);
  }
  
  printf("\n%stext = ", is_decrypt ? PLAIN_STR : CIPHER_STR);
	for(i=0;i<len;i++)
		printf("%02x", input[i]);
	printf("\n");
  if (is_decrypt)
    printf("\nplaintext = %s\n", input);
}

int main(int argc, char **argv)
{
  int is_decrypt = 0, is_iv = 0;
	if(argc < 2 || argv[1][0] != '-')
	{
		usage();
		return 1;
	}
  memset(iv, 0, sizeof(iv));
	switch(argv[1][1])
	{
    case 'c':
    case 'C':
      is_iv = 1;
		case 'e':
		case 'E': 
			is_decrypt = 0;
			break;
		case 'b':
		case 'B':
      is_iv = 1;
    case 'd':
		case 'D':
			is_decrypt = 1;
			break;
		default:
			usage();
			return 1;
	}
  if (is_iv)
    read_iv();
  crypt(is_decrypt, is_iv);
	return 0;
}
