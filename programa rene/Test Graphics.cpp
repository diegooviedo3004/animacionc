#include<graphics.h>
#include<stdio.h>
#include<conio.h>
#include <unistd.h>

int main(void) {
  int gdriver = DETECT, gmode;
  int i = 0;
  initgraph(&gdriver, &gmode, "c:\TC20\BIN");
while(1==1){
getch();
  cleardevice();
  getch();
  closegraph();   
}

