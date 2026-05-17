#include <stdio.h>

int half(int a,int b){
    int s = (a|b)&(~(a&b));
    int c = a&b;
    return s, c;
}

int all(int a, int b, int x){
    int s1,c1 = half(a,b);
    int s2,c2 = half(s1,x);
    int c = c1|c2;
    int s = s2;
    return s, c;
}

int main(){
    int a;
    scanf("%d", &a);
    int b;
    scanf("%d", &b);
    printf("%d",all(a,b,0));
}