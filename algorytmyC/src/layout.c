#include <math.h>
#include <stdlib.h>
#include <time.h>
#include "layout.h"
#ifndef M_PI
#define M_PI 3.14159
#endif

void circle_layout(double *x, double *y, int n) {
    for (int i = 0; i < n; i++) {
        double angle = 2.0 * M_PI * i / n;
        x[i] = 100.0 * cos(angle);
        y[i] = 100.0 * sin(angle);
    }
}
void random_layout(double *x, double *y, int n) {
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        x[i] = (rand() % 2000) / 10.0 - 100.0; 
        y[i] = (rand() % 2000) / 10.0 - 100.0;
    }
}




