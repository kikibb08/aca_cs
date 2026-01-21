#include <stdio.h>
int guess;
void createandfill(){
    int array [100];
    for (int i=0;i<100;i++){
        array[i]=i;
    }
}
void search(){
    scanf("%d", &guess);
    for (int i=0;i<100;i++){
        if (guess==i){
            printf("\n Your input has the index value %d", i);
        }
    }
}
int main(){
    createandfill();
    search();
}