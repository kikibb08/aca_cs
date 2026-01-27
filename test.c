#include <stdio.h>
void _0_10(){
    for (int i=0;i<=10; i++){
        printf ("%d ",i);}
    }
void _2_20(){
    for (int i=2;i<=20; i++){
        printf("%d ", i);}
}
void even_4_40(){
    for (int i=2; i<=20; i++){
        printf("%d ", (i*2));
    }
}
void odd_101_303(){
    for (int i=50; i<=151; i++){
        printf("%d ", (i*2)+1);
    }
}
void seven_multiples(){
    for (int i=1; i<=10; i++){
        printf("%d ", (i*7));
    }
}
 int main(){
     _0_10();
     printf("\n");
     _2_20();
     printf("\n");
     even_4_40();
     printf("\n");
     odd_101_303();
     printf("\n");
     seven_multiples();
     printf("\n");
 }
