#include <stdio.h>
#include <string.h>
#include "md5.h"

void main(void) 
{
  unsigned char input[1024];
  unsigned char path[1024];
  unsigned char digest[16]; //存放结果
  int i;
  
  printf("\ninput plaintext:");
	scanf("%s", input);
  printf("\ninput path:");
	scanf("%s", path);
  
  //第一种用法: 
  
  MD5_CTX md5c; 
  MD5Init(&md5c); //初始化 
  MD5UpdaterString(&md5c,input); 
  MD5FileUpdateFile(&md5c,path); 
  MD5Final(digest,&md5c); 
  
  //第二种用法: 
  MDString(input,digest); //直接输入字符串并得出结果 
  for(i = 0; i < 16; i++)
	{
		printf("%02x", digest[i]);
	}
 //第三种用法: 
 MD5File(path,digest); //直接输入文件路径并得出结果 
} 
