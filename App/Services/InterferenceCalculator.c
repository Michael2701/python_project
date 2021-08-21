#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

char** str_split(char* a_str, const char a_delim);

void main(int argc, char* argv[]){
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    char keys_list[27][4] = {"AAA", "AAB", "AAH", "ABA", "ABB", "ABH", "AHA", "AHB", "AHH",
                            "BAA", "BAB", "BAH", "BBA", "BBB", "BBH", "BHA", "BHB", "BHH",
                            "HAA", "HAB", "HAH", "HBA", "HBB", "HBH", "HHA", "HHB", "HHH"};

    char buffer[200];    
    float marker_differences[10000][2];
    long markers_counter = 0;
    long double N_00 = 0;
    long double N_01 = 0;
    long double N_10 = 0;
    long double N_11 = 0;
    char** chunks;



    if(argc >= 2){
        fp = fopen(argv[1], "r");
        if (fp == NULL){
            printf("Suka pochemu ty ne rabotaesh???");
            exit(EXIT_FAILURE);
        }

        while ((read = getline(&line, &len, fp)) != -1) {

            chunks = str_split(line, ',');

            if (chunks)
            {
                for (int i = 0; *(chunks + i); i++)
                {
                    if(i > 2 && i < 6){
                        char* ptr;
                        if(i == 3)
                            marker_differences[markers_counter][0] = -1 * strtof(chunks[i], &ptr);

                        if(i == 4){
                            marker_differences[markers_counter][0] += strtof(chunks[i], &ptr);      
                            marker_differences[markers_counter][1] = -1 * strtof(chunks[i], &ptr);
                        }

                        if(i == 5){
                            marker_differences[markers_counter][1] += strtof(chunks[i], &ptr);
                            markers_counter++;
                        } 
                    }
                    

                    if(i > 5){
                        // === COUNTERS ===
                        
                        // N_00: AAA, BBB
                        if(i == 6 || i == 19)
                            // N_00: AAA, BBB
                            N_00 += atof(chunks[i]);

                        // N_10: ABB, BAA
                        if(i == 10 || i == 15)
                            N_10 += atof(chunks[i]);

                        // # N_01: AAB, BBA
                        if(i == 7 || i == 15)
                            N_10 += atof(chunks[i]);

                        // N_11: ABA, BAB
                        if(i == 9 || i == 16)
                            N_11 += atof(chunks[i]);

                        // === DISTRIBUTION ===

                        // AAH, BBH: 00, 01
                        if(i == 8 || i == 20){
                            N_01 += atof(chunks[i]) / 2.0;
                            N_00 += atof(chunks[i]) / 2.0;
                        }

                        // HAA, HBB: 00, 10 
                        if(i == 24 || i == 28){
                            N_00 += atof(chunks[i]) / 2.0;
                            N_10 += atof(chunks[i]) / 2.0;
                        }

                        // ABH, BAH: 10, 11
                        if(i == 11 || i == 17){
                            N_10 += atof(chunks[i]) / 2.0;
                            N_11 += atof(chunks[i]) / 2.0;
                        }

                        // AHA, BHB: 00, 11
                        if(i == 12 || i == 22){
                            N_11 += atof(chunks[i]) / 2.0;
                            N_00 += atof(chunks[i]) / 2.0;
                        }
                        
                        // AHB, BHA: 01, 10
                        if(i == 13 || i == 21){
                            N_01 += atof(chunks[i]) / 2.0;
                            N_10 += atof(chunks[i]) / 2.0;
                        }

                        // HAB, HBA: 01, 11
                        if(i == 25 || i == 27){
                            N_01 += atof(chunks[i]) / 2.0;
                            N_11 += atof(chunks[i]) / 2.0;
                        }

                        // HAH, HBH:  00, 01, 11
                        if(i == 26 || i == 29){
                            N_00 += atof(chunks[i]) / 4.0;
                            N_01 += atof(chunks[i]) / 4.0;
                            N_11 += atof(chunks[i]) / 4.0;
                        }
                        
                        // AHH, BHH, HHA, HHB: 00, 01, 10, 11
                        if(i == 11 || i == 20 || i == 21 || i == 28){
                            N_00 += atof(chunks[i]) / 4.0;
                            N_01 += atof(chunks[i]) / 4.0;
                            N_10 += atof(chunks[i]) / 4.0;
                            N_11 += atof(chunks[i]) / 4.0;
                        }
                        
                        // HHH: 00, 01, 10, 11
                        if(i == 29){
                            N_00 += atof(chunks[i]) / 8.0;
                            N_01 += atof(chunks[i]) / 8.0;
                            N_10 += atof(chunks[i]) / 8.0;
                            N_11 += atof(chunks[i]) / 8.0;
                        }
                    }

                    free(*(chunks + i));
                }

                free(chunks);
            }
        }

        fclose(fp);
        if (line)
            free(line);

        printf("%Lf, %Lf, %Lf, %Lf, counter: %li \n", N_00, N_01, N_10, N_11, markers_counter);

        for(int x = 0; x < markers_counter; x++){
             printf("[%f, %f] ", marker_differences[x][0], marker_differences[x][1]);
        }


        system ("python App/myscript.py arg1 arg2");
        exit(EXIT_SUCCESS);
    }
}

char** str_split(char* a_str, const char a_delim)
{
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}




