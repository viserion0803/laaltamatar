#include<stdio.h>
#include<string.h>
int main()
{char buff[15];
int pass=0;
printf("enter the password\n");
gets(buff);
if(strcmp(buff,"the buffer stuff")){
    printf("\n wrong password\n");
}
else{
    printf("\ncorrect password\n");
    pass=1;
}
if(pass){
    printf("\nroot provilages given to the user\n");
}
else{
    printf("buffer overflow attack - - - -");
}
return 0;
}




