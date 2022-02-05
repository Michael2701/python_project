/* Header file */

#ifndef INTERFERENCE_CALCULATOR_H
#define INTERFERENCE_CALCULATOR_H

/* Standard libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <limits.h>

/* Constants */
#define TRUE 1
#define FALSE 0

/* Function declarations */
void fill_n_xx(int argc, char* argv[]);
void calculateLikelyHood();
void calculateLikelyHoodGradient();
void calculateXi();
void createOutputCSV(char* tripletOfGensFileName, char* interferenceFileName);
FILE *openFile(char* fileName, char* mode);

typedef struct
{
    double n_00;
    double n_01;
    double n_10;
    double n_11;
} TripleGenes;

#endif