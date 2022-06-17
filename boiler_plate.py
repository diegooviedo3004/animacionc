graphics_c_inicio = """#include<graphics.h>
#include<stdio.h>
#include<conio.h>
#include <unistd.h>

int main(void) {
  int gdriver = DETECT, gmode;
  int i = 0;
  initgraph(&gdriver, &gmode, "c:\\TC20\\BIN");
"""

graphics_c_final = """ 
getch();
  cleardevice();
  getch();
  closegraph();   
}
"""