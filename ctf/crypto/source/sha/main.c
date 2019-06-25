/* a simple test program of IDEA encryption and decryption. 
 * Author shenyang
 * */
#include <stdio.h>
#include <string.h>
#include "sha.h"

void usage()
{
	printf("Usage: sha SHAversion[0:sha-1,1:sha-224,2:sha-256,3:sha-384,4:sha-512]\n");
}

int main(int argc, char **argv)
{
  USHAContext ctx;
  uint8_t Message_Digest[USHAMaxHashSize];
  uint8_t bytes[1024];
  int i;
	if(argc < 2)
	{
		usage();
		return 1;
	}
  int version = atoi(argv[1]);
  printf("\ninput plaintext:");
	scanf("%s", bytes);
  USHAReset(&ctx, version);
  USHAInput(&ctx, bytes, strlen(bytes));
  USHAResult(&ctx,Message_Digest);
  for(i = 0; i < USHAHashSize(version) ; ++i)
    printf("%02X ", Message_Digest[i]);
  printf("\n");

	return 0;
}
