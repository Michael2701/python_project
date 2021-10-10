#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include <limits.h>

#include "utils.h"

#define N 10000
#define M 2

/*** Function declarations ***/
void calculateLikelyHood();
void calculateLikelyHoodGradient();
void calculateXi();
void createOutputCSV(char* tripletOfGensFileName, char* interferenceFileName);
FILE *openFile(char* fileName, char* mode);


/*** Variables ***/
double marker_differences[N][M];
long markers_counter = 0;

typedef struct
{
    double N_00;
    double N_01;
    double N_10;
    double N_11;
} TripleGenes;

TripleGenes N_xx[N];

double likelyHood[N];
double likelyHoodMaximum[N];
double max_coefficients[N];
double lrScore[N];

int main(int argc, char* argv[])
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    char** chunks;
    char* ptr;

    if(argc >= 3){
        fp = openFile(argv[1], "r");
        read = getline(&line, &len, fp); // skip results from first line

        while ((read = getline(&line, &len, fp)) != -1) {

            chunks = str_split(line, ',');

            if (chunks)
            {
                int i;
                for (i = 0; *(chunks + i); i++)
                {
                    if(i > 2 && i < 6) //
                    {

                        if(i == 3)
                            marker_differences[markers_counter][0] = -1 * strtof(chunks[i], &ptr) / 100;

                        if(i == 4){
                            marker_differences[markers_counter][0] += strtof(chunks[i], &ptr) / 100;
                            marker_differences[markers_counter][1] = -1 * strtof(chunks[i], &ptr) / 100;
                        }

                        if(i == 5){
                            marker_differences[markers_counter][1] += strtof(chunks[i], &ptr) / 100;
                            markers_counter++;
                        }
                    }


                    if(i > 5){
                        // === COUNTERS ===

                        // N_00: AAA, BBB
                        if(i == 6 || i == 19)
                            // N_00: AAA, BBB
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]);

                        // N_10: ABB, BAA
                        if(i == 10 || i == 15)
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]);

                        // # N_01: AAB, BBA
                        if(i == 7 || i == 15)
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]);

                        // N_11: ABA, BAB
                        if(i == 9 || i == 16)
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]);

                        // === DISTRIBUTION ===

                        // AAH, BBH: 00, 01
                        if(i == 8 || i == 20){
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 2.0;
                        }

                        // HAA, HBB: 00, 10
                        if(i == 24 || i == 28){
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 2.0;
                        }

                        // ABH, BAH: 10, 11
                        if(i == 11 || i == 17){
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 2.0;
                        }

                        // AHA, BHB: 00, 11
                        if(i == 12 || i == 22){
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 2.0;
                        }

                        // AHB, BHA: 01, 10
                        if(i == 13 || i == 21){
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 2.0;
                        }

                        // HAB, HBA: 01, 11
                        if(i == 25 || i == 27){
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 2.0;
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 2.0;
                        }

                        // HAH, HBH:  00, 01, 10, 11
                        if(i == 26 || i == 29){
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 4.0;
                        }

                        // AHH, BHH, HHA, HHB: 00, 01, 10, 11
                        if(i == 11 || i == 20 || i == 21 || i == 28){
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 4.0;
                        }

                        // HHH: 00, 01, 10, 11
                        if(i == 29){
                            N_xx[markers_counter - 1].N_00 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_01 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_10 += atof(chunks[i]) / 4.0;
                            N_xx[markers_counter - 1].N_11 += atof(chunks[i]) / 4.0;
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

        calculateLikelyHoodGradient();
        calculateXi();
        createOutputCSV(argv[1], argv[2]);

        char python_command[100] = "python App/myscript.py ";
        int command_length = strlen(python_command);

        for(int f = 2, q = 0; f < argc; f++){
            for(int x = strlen(argv[f]), d = 0; x ; x--, d++, q++){
                python_command[command_length+q] = argv[f][d];
            }
            python_command[command_length + q++] = ' ';
        }

        system (python_command);
        exit(EXIT_SUCCESS);
    }

    return 0;
}

/**
* This function calculate likely hood when coefficient in range [0, 2].
*
*/
void calculateLikelyHoodGradient()
{
    double max_log_value, temp_log_value;
    double P_00, P_10, P_01, P_11;
    double max_coefficient_value;

    int i;
    for(i = 0; i < markers_counter; i++)
    {
        max_log_value = LONG_MIN;
        max_coefficient_value = 0;

        double coefficient;
        for(coefficient = 0.01; coefficient < 15; coefficient += 0.01)
        {
            P_00 = 1 - marker_differences[i][0] - marker_differences[i][1] + coefficient * marker_differences[i][0] * marker_differences[i][1];
            P_01 = marker_differences[i][1] - coefficient * marker_differences[i][0] * marker_differences[i][1];
            P_10 = marker_differences[i][0] - coefficient * marker_differences[i][0] * marker_differences[i][1];
            P_11 = coefficient * marker_differences[i][0] * marker_differences[i][1];

            temp_log_value = log(P_00) * N_xx[i].N_00 + log(P_01) * N_xx[i].N_01 + log(P_10) * N_xx[i].N_10 + log(P_11) * N_xx[i].N_11;

            if(fabs(coefficient - 1) < 0.001) // Mean: coefficient == 1 (double numbers version)
            {
                *(likelyHood + i) = temp_log_value;
            }
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

/**
 * This function create and write main variables to csv file.
 */
void createOutputCSV(char* tripletOfGensFileName, char* interferenceFileName)
{
    size_t len = 0;
    ssize_t read;
    char** cells;
    char* line = NULL;
    FILE* tripletOfGensFile;
    FILE* interferenceFile;

    tripletOfGensFile = openFile(tripletOfGensFileName, "r");
    interferenceFile = openFile(interferenceFileName, "w+");

    if(tripletOfGensFile && interferenceFile)
    {
        fprintf(interferenceFile, "marker 1,marker 2,marker 3,r1,r2,N_00,N_01,N_10,N_11,C max,log(C max),log(C=1),Xi\n"); // Print Header
        read = getline(&line, &len, tripletOfGensFile); // skip results from first line

        int i;
        for(i = 0; i < markers_counter && (read = getline(&line, &len, tripletOfGensFile)) != -1; i++)
        {
            cells = str_split(line, ',');
            fprintf(interferenceFile, "%s,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                cells[0], cells[1], cells[2],
                marker_differences[i][0], marker_differences[i][1],
                N_xx[i].N_00, N_xx[i].N_01, N_xx[i].N_10, N_xx[i].N_11,
                max_coefficients[i], likelyHoodMaximum[i],
                likelyHood[i], lrScore[i]); // markers * 3, r1, r2, N_00, N_01, N_10, N_11, C max, log(C max), log(C=1), Xi
        }

        fclose(interferenceFile);
        fclose(tripletOfGensFile);
    }
}

/**
* This function open output file
*/
FILE *openFile(char *fileName, char *mode)
{
    FILE *file = fopen(fileName, mode);

    if(!file)
    {
        printf("Error: can't open/create file\n");
        exit(EXIT_FAILURE);
    }
    else
    {
        return file;
    }
}
