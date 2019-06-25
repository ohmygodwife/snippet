#include <stdio.h>
#include <string.h>
#include "md5.h"

unsigned char dist[] = "0123456789abcdef";

unsigned char target[] = {
  0xC4, 0xE9, 0xEF, 0x81, 0x52, 0xF6, 0x1F, 0x53, 0x17, 0x5C, 
  0x76, 0x41, 0x89, 0xD1, 0x73, 0x7F
};

/*
{
  0xDC, 0x07, 0x8B, 0x85, 0xAD, 0xFD, 0xF9, 0xC1, 0x1B, 0x05, 
  0x02, 0x44, 0xEF, 0x4C, 0xFB, 0xDD
};
*/

void main(void) 
{
  MD5_CTX md5c;
  int i0, i1, i2, i3, i4, i5, i6, i7,j, len = strlen(dist);
  char input[9];
  
  input[8] = '\0';
  memset(input, '0', 8);
  
  for (i0 = 0; i0 < len; i0 ++)
    for (i1 = 0; i1 < len; i1 ++)
      for (i2 = 0; i2 < len; i2 ++)
        for (i3 = 0; i3 < len; i3 ++)
          for (i4 = 0; i4 < len; i4 ++)
            for (i5 = 0; i5 < len; i5 ++)
              for (i6 = 0; i6 < len; i6 ++)
                for (i7 = 0; i7 < len; i7 ++)
                {
                  input[0] = dist[i0];
                  input[1] = dist[i1];
                  input[2] = dist[i2];
                  input[3] = dist[i3];
                  input[4] = dist[i4];
                  input[5] = dist[i5];
                  input[6] = dist[i6];
                  input[7] = dist[i7];
                  printf("%s\n", input);
                  mspecInit(&md5c);
                  mspec(&md5c, input);
                  if (memcmp(md5c.state, target, 16) == 0)
                  {
                    break;
                  }
                }
  
} 
