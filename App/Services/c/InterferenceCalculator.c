// Compile file with: gcc -o InterferenceCalculator InterferenceCalculator.c utils.o -lm

#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include "utils.h"

#define N 10000
#define M 2

//void calculateLikelyHood(float marker_differences[][M], long markers_counter, float likelyHood[], float N_00, float N_01, float N_10, float N_11);
void calculateLikelyHood(double marker_differences[][M], long markers_counter, double * likelyHood, double N_00, double N_01, double N_10, double N_11)
{
    double coefficient = 1;
    double P_00, P_10, P_01, P_11;

    int i;
    for(i = 0; i < markers_counter; i++)
    {
        P_00 = fabs(1 - marker_differences[i][0] - marker_differences[i][1] + coefficient * marker_differences[i][0] * marker_differences[i][1]);
        P_01 = fabs(marker_differences[i][1] - coefficient * marker_differences[i][0] * marker_differences[i][1]);
        P_10 = fabs(marker_differences[i][0] - coefficient * marker_differences[i][0] * marker_differences[i][1]);
        P_11 = fabs(coefficient * marker_differences[i][0] * marker_differences[i][1]);

// test
//      printf("%f %f %f %f\n", P_00, P_01, P_10, P_11);
//      printf("%f %f %f %f\n", log(P_00), log(P_01), log(P_10), log(P_11));

        *(likelyHood + i) = log(P_00) * N_00 + log(P_01) * N_01 + log(P_10) * N_10 + log(P_11) * N_11;
    }

}

void main(int argc, char* argv[]){
    double marker_differences[N][M];
    double likelyHood[N];

    long markers_counter = 0;

    double N_00 = 0;
    double N_01 = 0;
    double N_10 = 0;
    double N_11 = 0;

    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    char** chunks;
    char* ptr;

    char keys_list[27][4] = {"AAA", "AAB", "AAH", "ABA", "ABB", "ABH", "AHA", "AHB", "AHH",
                            "BAA", "BAB", "BAH", "BBA", "BBB", "BBH", "BHA", "BHB", "BHH",
                            "HAA", "HAB", "HAH", "HBA", "HBB", "HBH", "HHA", "HHB", "HHH"};

    if(argc >= 2){
        fp = fopen(argv[1], "r");
        if (fp == NULL){
            printf("Error: Can't open file.csv\n");
            exit(EXIT_FAILURE);
        }

        while ((read = getline(&line, &len, fp)) != -1) {

            chunks = str_split(line, ',');

            if (chunks)
            {
                int i;
                for (i = 0; *(chunks + i); i++)
                {
                    if(i > 2 && i < 6){

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


// test
//        for(int x = 0; x < markers_counter; x++){
//             printf("[%f, %f] ", marker_differences[x][0], marker_differences[x][1]);
//        }

        calculateLikelyHood(marker_differences, markers_counter, likelyHood, N_00, N_01, N_10, N_11);

// test
        int i;
        for(i = 0; i < markers_counter; i++)
        {
           printf("%f ", *(likelyHood + i));
        }

        // system ("python App/myscript.py arg1 arg2");
        exit(EXIT_SUCCESS);
    }
}
