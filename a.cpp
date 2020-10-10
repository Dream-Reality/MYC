#include<bits/stdc++.h>
using namespace std;
void printbit(int x,int l){
  if (l==0)return;
  printbit(x>>1,l-1);
  printf("%d",x&1);
}
void print(char*c,int l){
  for (int i=0;i<l;i++,c++){
    printbit(*c,8);puts("");
  }
}
int main(){
  int x=0x12345678;
  char *c = (char*)&x;
  print(c,4);
}