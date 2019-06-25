#include <stdio.h>
#include <string.h>
#include "md4.h"

void main(void) 
{
  unsigned char input[1024];
//  unsigned char path[1024];
  unsigned char digest[16]; //存放结果
  int i;
  
  printf("\ninput plaintext:");
	scanf("%s", input);
//  printf("\ninput path:");
//	scanf("%s", path);
  
  MD4_CTX ctx; 
  MD4Init(&ctx); //初始化
  MD4Update(&ctx, input, strlen(input));
  MD4Final(digest,&ctx); 
  
  for(i = 0; i < 16; i++)
	{
		printf("%02x", digest[i]);
	}
} 
