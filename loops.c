#include <stdio.h>
void array(){
    int array[85];
}
void matrix(){
    int matrix[20][20];
}

void populatedarray(){
    for(int i=0; i<85;i++){
        int array[i];
    }
}
void populatedmatrix(){
    for (int i=0;i<20;i++){
        for(int j=0; j<20; j++){
            int matrix[i][j];
            printf("(%d,%d) ", i, j);
        }
    }
}
int main(){
    array();
    matrix();
    populatedarray();
    populatedmatrix();
}