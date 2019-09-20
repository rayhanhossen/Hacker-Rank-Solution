#include<stdio.h>
#include<string.h>
#define MX 100

int main(){
    
    char ch;
    char s[MX];
    char sen[MX];

    scanf("%c",&ch);
    scanf("%s",s);
    scanf("\n");
    scanf("%[^\n]%*c",sen);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n",sen);

}