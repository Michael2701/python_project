/*
 * This file contain mathematics genetic calculation on genetic data.
 * Logarithmic calculations, likelihood calculation and statistic calculations.
 * 
 * Language:  C
 */

#include "interference_calculator.h"
#include "utils.h"

/*** Constants ***/
#define N 10000
#define M 2

#define TWO 2.0
#define FOUR 4.0
#define ONE_HUNDRED 100

double marker_differences[N][M];
long markers_counter = 0;

TripleGenes n_xx[N];

double likelyHood[N];
double likelyHoodMaximum[N];
double max_coefficients[N];
double lrScore[N];

int main(int argc, char* argv[])
{
    if(argc >= 3)
    {
        fill_n_xx(argc, argv);
        calculateLikelyHoodGradient();
        calculateXi();
        createOutputCSV(argv[1], argv[2]);

        char python_command[ONE_HUNDRED] = "python3 back_from_C.py ";
        int command_length = strlen(python_command);

        for(int f = 2, q = 0; f < argc; f++){
            for(int x = strlen(argv[f]), d = 0; x ; x--, d++, q++){
                python_command[command_length+q] = argv[f][d];
            }
            python_command[command_length + q++] = ' ';
        }
        system(python_command);
        exit(EXIT_SUCCESS);
    }
    return 0;
}

/* */
void fill_n_xx(int argc, char* argv[])
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

        while ((read = getline(&line, &len, fp)) != EOF) {

            chunks = str_split(line, ',');

            if (chunks)
            {
                // i - this is position in array:
                // marker 1,marker 2,marker 3,position 1,position 2,position 3,AAA,AAB,AAH,ABA,ABB,ABH,AHA,AHB,AHH,BAA,BAB,BAH,BBA,BBB,BBH,BHA,BHB,BHH,HAA,HAB,HAH,HBA,HBB,HBH,HHA,HHB,HHH
                float temp;
                int i;
                for (i = 3; *(chunks + i); i++) // we start from i = 3 (position 1)
                {
                    if(i >= 3 && i <= 5) //
                    {
                        if(i == 3) // position 1
                        {
                            marker_differences[markers_counter][0] = -1 * strtof(chunks[i], &ptr) / ONE_HUNDRED;
                        }

                        else if(i == 4) // position 2
                        {
                            marker_differences[markers_counter][0] += strtof(chunks[i], &ptr) / ONE_HUNDRED;
                            marker_differences[markers_counter][1] = -1 * strtof(chunks[i], &ptr) / ONE_HUNDRED;
                        }

                        else if(i == 5) // position 3
                        {
                            marker_differences[markers_counter][1] += strtof(chunks[i], &ptr) / ONE_HUNDRED;
                            markers_counter++;
                        }
                    }
                    else
                    {
                        // === COUNTERS ===

                        // n_00: AAA, BBB
                        if(i == 6 || i == 19)
                            // n_00: AAA, BBB
                            n_xx[markers_counter - 1].n_00 += atof(chunks[i]);

                        // n_10: ABB, BAA
                        if(i == 10 || i == 15)
                            n_xx[markers_counter - 1].n_10 += atof(chunks[i]);

                        // # n_01: AAB, BBA
                        if(i == 7 || i == 15)
                            n_xx[markers_counter - 1].n_01 += atof(chunks[i]);

                        // n_11: ABA, BAB
                        if(i == 9 || i == 16)
                            n_xx[markers_counter - 1].n_11 += atof(chunks[i]);

                        // === DISTRIBUTION ===

                        // AAH, BBH: 00, 01
                        if(i == 8 || i == 20){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_01 += temp;
                            n_xx[markers_counter - 1].n_00 += temp;
                        }

                        // HAA, HBB: 00, 10
                        else if(i == 24 || i == 28){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_00 += temp;
                            n_xx[markers_counter - 1].n_10 += temp;
                        }

                        // ABH, BAH: 10, 11
                        else if(i == 11 || i == 17){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_10 += temp;
                            n_xx[markers_counter - 1].n_11 += temp;
                        }

                        // AHA, BHB: 00, 11
                        else if(i == 12 || i == 22){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_11 += temp;
                            n_xx[markers_counter - 1].n_00 += temp;
                        }

                        // AHB, BHA: 01, 10
                        else if(i == 13 || i == 21){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_01 += temp;
                            n_xx[markers_counter - 1].n_10 += temp;
                        }

                        // HAB, HBA: 01, 11
                        else if(i == 25 || i == 27){
                            temp = atof(chunks[i]) / TWO;
                            n_xx[markers_counter - 1].n_01 += temp;
                            n_xx[markers_counter - 1].n_11 += temp;
                        }

                         // HAH, HBH:  00, 01, 10, 11
                         // AHH, BHH, HHA, HHB: 00, 01, 10, 11
                         // HHH: 00, 01, 10, 11
                        else
                        {
                            temp = atof(chunks[i]) / FOUR;
                            n_xx[markers_counter - 1].n_00 += temp;
                            n_xx[markers_counter - 1].n_01 += temp;
                            n_xx[markers_counter - 1].n_10 += temp;
                            n_xx[markers_counter - 1].n_11 += temp;
                        }

//                        // HAH, HBH:  00, 01, 10, 11
//                        if(i == 26 || i == 29)
//                        {
//                            n_xx[markers_counter - 1].n_00 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_01 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_10 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_11 += atof(chunks[i]) / FOUR;
//                        }
//
//                        // AHH, BHH, HHA, HHB: 00, 01, 10, 11
//                        if(i == 11 || i == 20 || i == 21 || i == 28){
//                            n_xx[markers_counter - 1].n_00 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_01 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_10 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_11 += atof(chunks[i]) / FOUR;
//                        }
//
//                        // HHH: 00, 01, 10, 11
//                        if(i == 29){
//                            n_xx[markers_counter - 1].n_00 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_01 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_10 += atof(chunks[i]) / FOUR;
//                            n_xx[markers_counter - 1].n_11 += atof(chunks[i]) / FOUR;
//                        }
                    }

                    free(*(chunks + i));
                }

                free(chunks);
            }
        }

        fclose(fp);
        if (line)
            free(line);
    }

    return;
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

            temp_log_value = log(P_00) * n_xx[i].n_00 + log(P_01) * n_xx[i].n_01 + log(P_10) * n_xx[i].n_10 + log(P_11) * n_xx[i].n_11;

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
        fprintf(interferenceFile, "marker 1,marker 2,marker 3,r1,r2,n_00,n_01,n_10,n_11,C max,log(C max),log(C=1),Xi\n"); // Print Header
        read = getline(&line, &len, tripletOfGensFile); // skip results from first line

        int i;
        for(i = 0; i < markers_counter && (read = getline(&line, &len, tripletOfGensFile)) != -1; i++)
        {
            cells = str_split(line, ',');
            fprintf(interferenceFile, "%s,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                cells[0], cells[1], cells[2],
                marker_differences[i][0], marker_differences[i][1],
                n_xx[i].n_00, n_xx[i].n_01, n_xx[i].n_10, n_xx[i].n_11,
                max_coefficients[i], likelyHoodMaximum[i],
                likelyHood[i], lrScore[i]); // markers * 3, r1, r2, n_00, n_01, n_10, n_11, C max, log(C max), log(C=1), Xi
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
