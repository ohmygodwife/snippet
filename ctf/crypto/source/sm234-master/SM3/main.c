#include <stdio.h>
#include <string.h>
#include "sm3.h"

void main(void) 
{
  unsigned char input[1024];
  unsigned char path[1024];
  unsigned char output[32]; //存放结果
  int i;
  
  printf("\ninput plaintext:");
	scanf("%s", input);
  
  //第一种用法: 
  
  sm3_context ctx; 
  sm3_starts( &ctx );
  sm3_update( &ctx, input, strlen(input) ); 
  sm3_finish( &ctx, output );
  
  for(i = 0; i < 32; i++)
	{
		printf("%02x", output[i]);
	}
  printf("\n");
  
  //第二种用法: 
  sm3(input, strlen(input), output); //直接输入字符串并得出结果 
  for(i = 0; i < 32; i++)
	{
		printf("%02x", output[i]);
	}
} 
