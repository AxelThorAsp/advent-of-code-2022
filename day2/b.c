
#include <stdio.h>
#include <stdlib.h>


#define ROCK 'A'
#define PAPER 'B'
#define SCISSORS 'C'


int R = 1;
int P = 2;
int S = 3;


int score(char a, char b) {
    if (a == ROCK) {
        if (b == 'X') return 0 + S;
        if (b == 'Y') return 3 + R;
        if (b == 'Z') return 6 + P;
    }
    else if (a == PAPER) {
        if (b == 'X') return 0 + R;
        if (b == 'Y') return 3 + P;
        if (b == 'Z') return 6 + S;
    }
    else if (a == SCISSORS) {
        if (b == 'X') return 0 + P;
        if (b == 'Y') return 3 + S;
        if (b == 'Z') return 6 + R;
    }
    return 0;
}


int main (int argc, char **argv) {
   char a, b;
   FILE *fp;
   char *filepath = argv[1];
   int sum = 0;

   fp = fopen(filepath, "r+");

   if (!fp) {
       exit(1);
   }
   while(fscanf(fp, " %c %c", &a, &b) != EOF) {
       sum += score(a,b);
   }

   printf("%d\n",sum);

   fclose(fp);
   return(0);
}
