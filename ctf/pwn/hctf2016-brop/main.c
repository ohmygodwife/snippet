#include <stdio.h>
#include <unistd.h>
#include <string.h>
int i;
int check();
int main(void){
	setbuf(stdin,NULL);
	setbuf(stdout,NULL);
	setbuf(stderr,NULL);
    write(STDOUT_FILENO, "WelCome my friend,Do you know password?\n", 40);
	if(!check()){
        fputs("Do not dump my memory", stdout);
	}else {
        puts("No password, no game");
	}
}
int check(){
    char buf[50];
    read(STDIN_FILENO,buf,1024);
    return strcmp(buf,"aslvkm;asd;alsfm;aoeim;wnv;lasdnvdljasd;flk");
}
