#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void update(int *a, int *b){
    *a = *a + *b;
    *b = *a - (*b * 2);
}

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    update(&a, &b);
    printf("%d\n",a);
    printf("%d\n",abs(b));

    return 0;
}