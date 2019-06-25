#include<stdio.h>
void func()
{
    char name[0x50];
    read(0, name, 0x100);
    write(1, name, 0x100);
}
int main()
{
    func();
    return 0;
}