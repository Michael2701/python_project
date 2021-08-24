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

void calculateLikelyHood();
void calculateLikelyHoodGradient();
void calculateXi();
void createOutputCSV(char *fileName);
FILE *openFile(char *fileName);

double marker_differences[N][M];
long markers_counter = 0;

double N_00 = 0, N_01 = 0, N_10 = 0, N_11 = 0;
double likelyHood[N];
double likelyHoodMaximum[N];
double max_coefficients[N];
double lrScore[N];

void main(int argc, char* argv[])
{
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
            printf("Error: Can't open triplet_of_genes.csv\n");
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

        calculateLikelyHood();
        calculateLikelyHoodGradient();
        calculateXi();
        createOutputCSV(argv[2]);

        // system ("python App/myscript.py arg1 arg2");
        exit(EXIT_SUCCESS);
    }
}

void calculateLikelyHood()
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

        *(likelyHood + i) = log(P_00) * N_00 + log(P_01) * N_01 + log(P_10) * N_10 + log(P_11) * N_11;
    }

}

void calculateLikelyHoodGradient()
{
    double max_log_value, temp_log_value;
    double P_00, P_10, P_01, P_11;
    double max_coefficient_value;

    int i;
    for(i = 0; i < markers_counter; i++)
    {
        max_log_value = 0;
        max_coefficient_value = 0;

        double coefficient;
        for(coefficient = 0; coefficient < 2; coefficient += 0.01)
        {
            P_00 = fabs(1 - marker_differences[i][0] - marker_differences[i][1] + coefficient * marker_differences[i][0] * marker_differences[i][1]);
            P_01 = fabs(marker_differences[i][1] - coefficient * marker_differences[i][0] * marker_differences[i][1]);
            P_10 = fabs(marker_differences[i][0] - coefficient * marker_differences[i][0] * marker_differences[i][1]);
            P_11 = fabs(coefficient * marker_differences[i][0] * marker_differences[i][1]);

            temp_log_value = log(P_00) * N_00 + log(P_01) * N_01 + log(P_10) * N_10 + log(P_11) * N_11;

            if (temp_log_value > max_log_value)
            {
                max_log_value = temp_log_value;
                max_coefficient_value = coefficient;
            }
        }// End loop likelyHood gradient

        *(likelyHoodMaximum + i) = max_log_value;
        *(max_coefficients + i) = max_coefficient_value;
    }// End loop of distance between r1 and r2 markers
}// End function calculateLikelyHoodGradient

// Search df
void calculateXi()
{
    int i;
    for(i = 0; i < markers_counter; i++)
    {
        *(lrScore + i) = 2 * (likelyHood[i] - likelyHoodMaximum[i]);
    }
}

void createOutputCSV(char *fileName)
{
    FILE *file;
    if(file = openFile(fileName))
    {
        fprintf(file, "r1,r2,C,Xi\n"); // Print Header

        int i;
        for(i = 0; i < markers_counter; i++)
        {
            fprintf(file, "%f,%f,%f,%f\n",
            marker_differences[i][0], marker_differences[i][1], max_coefficients[i], lrScore[i]); // markers * 3, r1, r2, C, Xi
        }
    }
}

FILE *openFile(char *fileName)
{
    FILE *file = fopen(fileName, "w+");

    if(!file){
        printf("Error, can't open/create file");
        return NULL;
    }else{
        return file;
    }
}

FILE *openFileTripleGenes()
{
    FILE *file;

    return file;
}

