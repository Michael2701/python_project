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
void calculateLikelyHood();
void calculateLikelyHoodGradient();
void calculateXi();
void createOutputCSV(char* tripletOfGensFileName, char* interferenceFileName);
FILE *openFile(char* fileName, char* mode);

typedef struct
{
    double N_00;
    double N_01;
    double N_10;
    double N_11;
} TripleGenes;

#endif