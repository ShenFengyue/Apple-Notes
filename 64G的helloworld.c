#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <time.h>

//#define SIZE 17179869184 // Size of the arrays

#define SIZE 8589934592 // Size of the arrays

#define GB64 68719476736 // Size of the arrays

//GB64 68719476736

//GB32 34359738368

//GB16 17179869184

//GB08 8589934592

//GB01 1073741824

//M500 536870912

float *src; // Declare source array as a pointer

float dest[SIZE]; // Declare destination array as a global variable

int main() {

    size_t i;

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);

    src = (float *)malloc(SIZE * sizeof(float));

    if (src == NULL) {

        printf("Error: Could not allocate memory\n");

        return 1;

    }

    for (i = 0; i < SIZE; i++) {

        src[i] = (float)i / ( (float)i +1) ;

    }

    memcpy(dest, src, SIZE * sizeof(float));

    clock_gettime(CLOCK_MONOTONIC, &end);

    double elapsed_time = (end.tv_sec - start.tv_sec) + (double)(end.tv_nsec - start.tv_nsec) / 1000000000;

    printf("Time elapsed: %.2f seconds\n", elapsed_time);

    printf("Source array: ");

    for (i = 0; i < 10; i++) {

        printf("%.2f ", src[i]);

    }

    printf("\n");

    printf("Destination array: ");

    for (i = 0; i < 10; i++) {

        printf("%.2f ", dest[i]);

    }

    printf(" Hello World! \n");

    free(src);

    return 0;

}
