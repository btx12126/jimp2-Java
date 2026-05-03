#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

int read_graph(const char *filename, Edge **edges, int *n, int **exists)
{
    FILE *f = fopen(filename, "r");
    if (!f) return -1;

    int capacity = 10;
    int count = 0;
    int max_node = -1;

    Edge *e = malloc(capacity * sizeof(Edge));
    if (!e) { fclose(f); return -1; }

    int *ex = calloc(10000, sizeof(int));

    char name[64];
    int u, v;
    double w;

   while (fscanf(f, " %63s %d %d %lf", name, &u, &v, &w) == 4) {
    if (count >= capacity) {
        capacity *= 2;
        Edge *temp = realloc(e, capacity * sizeof(Edge));
        if (!temp) { free(e); free(ex); fclose(f); return -1; }
        e = temp;
    }
    e[count].u = u;
    e[count].v = v;
    e[count].weight = w;

    if (u < 10000) ex[u] = 1; 
    if (v < 10000) ex[v] = 1;

    if (u > max_node) max_node = u;
    if (v > max_node) max_node = v;
    count++;
}
fclose(f);

    if (count == 0) {
        free(e);
        free(ex);
        return 0;
    }

    *exists = ex;
    *edges = e;
    *n = (max_node < 0) ? 0 : max_node + 1;
    
    return count;
}




