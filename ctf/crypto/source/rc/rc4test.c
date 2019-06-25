/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "rc4.h"

int input_hex(unsigned char *inbuf, const char* hint)
{
  char str[8 * 1024 * 2];
  int len = 0;
  
  printf("\ninput %s(in hex):", hint);
	scanf("%s", str);
	len = 0;
  
  while(sscanf(str+len*2, "%02x", &(inbuf[len]))!=EOF)
		len++;

  return len;
}

void output_hex(unsigned char *outbuf, int len, const char* hint)
{
  int i;
  printf("\n%s(in hex) is: ", hint);
  for(i = 0; i < len; i++)
	{
		printf("%02x", outbuf[i]);
	}
  printf("\n%s text is: %s\n", hint, outbuf);
}

int main(int argc, char **argv)
{
  struct rc4_state state;
  unsigned char key[1024];
  unsigned char inbuf[8 * 1024];
  unsigned char outbuf[8 * 1024];
  int len;
  
  memset(key, 0, sizeof(key));
  memset(inbuf, 0, sizeof(inbuf));
  memset(outbuf, 0, sizeof(outbuf));
  
  len = input_hex(key, "key");
  rc4_init(&state, key, len);
  
  len = input_hex(inbuf, "ciphertext");
  rc4_crypt(&state, inbuf, outbuf, len);
  output_hex(outbuf, len, "plain");

	return 0;
}