#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char** str_split(char* a_str, const char a_delim)
{
    char **result;
    char* tmp        = a_str;
    char* last_comma = 0;
    char buffer[25];
    int count = 0;
    int i, j, y = 0;

    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    count += last_comma < (a_str + strlen(a_str) - 1);
    count++;

    result = (char**)malloc(sizeof(char*) * count);

    for(i = 0, j = 0; i < strlen(a_str); i++){
        if(a_str[i] != ','){
            buffer[j++] = a_str[i];
        }else{
            buffer[j] = '\0';
            char* b = (char*)malloc(sizeof(char)*strlen(buffer)+10);
            for(int r = 0; r < strlen(buffer); r++){
                b[r] = buffer[r];
            }
            result[y++] = b;
            j = 0;
        }
    }
    return result;
}

//void main(){
//    char a_str[100] = "mark,23,ab,bc,cd,de,t,y,u,i";
//    char a_delim = ',';
//
//    char** result = str_split(a_str, a_delim);
//
//
//
//    for (int i = 0; *(result + i); i++){
//        printf("%s \n", *(result + i));
//    }
//}

