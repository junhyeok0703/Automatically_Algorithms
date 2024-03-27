#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int s = n/10;
    int sum =0;
    sum= (n*12000)+((k-s)*2000);
    return sum;
}